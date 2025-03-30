from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Config


# Base declarative para os modelos
Base = declarative_base()

class DatabaseConnection:
    def __init__(self):
        """
        Inicializa a conexão com o banco de dados SQLite.

        :param db_path: Caminho para o arquivo do banco de dados SQLite. Se None, usa o caminho da Config.
        """
        self.engine = create_engine(f'sqlite:///{Config.DATABASE}')
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        """
        Gerencia o contexto da sessão com o banco de dados SQLAlchemy.
        Garante que a sessão será fechada após o uso.
        """
        return self.Session()

    def setup_database(self):
        """
        Cria todas as tabelas definidas nos modelos que herdam de Base
        """
        Base.metadata.create_all(self.engine)