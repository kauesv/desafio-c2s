from utils.database import seed_vehicles
from database.data_source import DatabaseConnection
from config import Config
import sys


def main():
    """
    Função principal para iniciar o servidor MCP
    """
    print("Iniciando o servidor de consulta de automóveis...")
    
    # Criando tabelas no banco de dados
    database = DatabaseConnection()
    database.setup_database()

    # Populando o banco de dados com dados fictícios
    seed_vehicles.popular_banco()

    print(f"Configurado para rodar em: {Config.HOST_SERVER}:{Config.PORT_SERVER}")

if __name__ == "__main__":
    main()