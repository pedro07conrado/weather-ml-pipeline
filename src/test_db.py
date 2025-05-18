from data.database import get_connection

conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
tables = cur.fetchall()
print("Tabelas encontradas:", tables)
cur.close()
conn.close()
