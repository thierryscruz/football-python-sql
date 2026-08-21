from dotenv import load_dotenv
import os
from pathlib import Path
import sys 

BASE_DIR = Path(__file__).parent

#Carregar o arquivo .env
load_dotenv(BASE_DIR / ".env")

#configuração de conexão com banco de dados
DB_URL = os.getenv("NEON_URL")
API_URL = os.getenv("API_URL")

#Lista de competições a serem monitoradas com seus respectivos IDs
COMPETITIONS = {
    "ID-BRA-SERIE-A": "bra.1",
    "ID-BRA-SERIE-B": "bra.2",
    "ID-CONMEBOL-COPA-LIBERTADORES": "conmebol.libertadores",
    "ID-CONMEBOL-COPA-SUDAMERICANA": "conmebol.sudamericana",
    "ID-ENG-PREMIER-LEAGUE": "eng.1",
    "ID-UEFA-CHAMPIONS-LEAGUE": "uefa.champions",    
}