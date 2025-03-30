from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # Banco
    DATABASE=os.getenv('DATABASE')

    # Configurações
    TZ=os.getenv('TZ')

    # Servidor
    HOST_SERVER=os.getenv('HOST_SERVER')
    PORT_SERVER=os.getenv('PORT_SERVER')