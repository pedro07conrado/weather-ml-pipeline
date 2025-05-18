import os
import pandas as pd
import joblib
from dotenv import load_dotenv
from sklearn.linear_model import LinearRegression
from src.data.database import get_connection
from sqlalchemy import create_engine 

load_dotenv()


def load_data():
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    engine = create_engine(db_url)
    query = "SELECT temperature, humidity FROM raw_data;"
    df = pd.read_sql(query, engine)
    return df

#def load_data():
#    conn = get_connection()
#    query = "SELECT temperature, humidity FROM raw_data;"
#    df = pd.read_sql(query, conn)
#    conn.close()
#    return df

def train_model(df):
    # Aqui vamos prever temperatura com base na umidade
    X = df[['humidity']]
    y = df['temperature']

    model = LinearRegression()
    model.fit(X, y)
    return model

def save_model(model):
    os.makedirs('models/trained', exist_ok=True)
    joblib.dump(model, 'models/trained/model.joblib')
    print("✅ Modelo salvo com sucesso em models/trained/model.joblib")

if __name__ == "__main__":
    df = load_data()
    if df.empty:
        print("❌ Nenhum dado encontrado no banco.")
    else:
        print(f"✅ Dados carregados: {df.shape[0]} registros")
        model = train_model(df)
        save_model(model)
