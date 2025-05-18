from data.api_client import get_weather_data
from data.database import get_connection
from datetime import datetime

def insert_weather_into_db():
    data = get_weather_data()
    if data:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO raw_data (city, temperature, humidity, timestamp)
            VALUES (%s, %s, %s, to_timestamp(%s))
        """, (
            data["city"],
            data["temperature"],
            data["humidity"],
            data["timestamp"]
        ))
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Dados inseridos com sucesso!")
    else:
        print("❌ Não foi possível obter os dados.")

if __name__ == "__main__":
    insert_weather_into_db()
