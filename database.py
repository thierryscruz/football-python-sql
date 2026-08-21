
# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine
from config import DB_URL
import psycopg2

engine = create_engine(DB_URL)

con = engine.connect()
print("Conexão com o banco de dados estabelecida com sucesso!")
con.close()