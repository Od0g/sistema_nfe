import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do .env

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '321d506ed2eb499a324fc48e1a054dfc845978c1bc61b86e'
    # Garanta que a URL é carregada corretamente aqui
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.strip().strip("'").strip('"')


    print(f"DEBUG: SQLALCHEMY_DATABASE_URI FINAL: {SQLALCHEMY_DATABASE_URI}")

    SQLALCHEMY_TRACK_MODIFICATIONS = False