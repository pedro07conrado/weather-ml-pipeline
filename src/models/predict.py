import joblib
import numpy as np
import os

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

if __name__ == "__main__":
    try:
        humidity = float(input("💧 Digite a umidade (%): "))
        temp = predict_temperature(humidity)
        print(f"🌡️ Temperatura prevista: {temp:.2f}°C")
    except Exception as e:
        print(f"❌ Erro: {e}")
