import joblib
import numpy as np
import os
import psycopg2
from datetime import datetime, timezone
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

def load_model():
    model_path = "models/trained/model.joblib"
    if not os.path.exists(model_path):
        raise FileNotFoundError("❌ Modelo não encontrado. Execute train.py antes.")
    return joblib.load(model_path)

def predict_temperature(humidity):
    model = load_model()
    X = np.array([[humidity]])
    prediction = model.predict(X)
    return prediction[0]

def save_prediction_to_db(humidity, predicted_temp):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5433"),
            database=os.getenv("DB_NAME", "weather"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres")
        )
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO model_predictions (humidity, predicted_temperature, timestamp)
            VALUES (%s, %s, %s);
        """
        cursor.execute(insert_query, (
            float(humidity),
            float(predicted_temp),
            datetime.now(timezone.utc)
        ))
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Predição salva no banco de dados com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao salvar no banco de dados: {e}")

if __name__ == "__main__":
    try:
        humidity = float(input("💧 Digite a umidade (%): "))
        temp = predict_temperature(humidity)
        print(f"🌡️ Temperatura prevista: {temp:.2f}°C")
        save_prediction_to_db(humidity, temp)
    except Exception as e:
        print(f"❌ Erro: {e}")
