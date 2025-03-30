from sqlalchemy import Column, Integer, String, Float
from database.data_source import Base


class Automovel(Base):
    __tablename__ = 'automoveis'
    
    id = Column(Integer, primary_key=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    motorizacao = Column(Float, nullable=False)
    tipo_combustivel = Column(String(20), nullable=False)
    cor = Column(String(30), nullable=False)
    quilometragem = Column(Integer, nullable=False)
    numero_portas = Column(Integer, nullable=False)
    transmissao = Column(String(20), nullable=False)
    preco = Column(Float, nullable=False)
    potencia = Column(Integer)
    torque = Column(Float)
    capacidade_porta_malas = Column(Integer)
    consumo_cidade = Column(Float)
    consumo_estrada = Column(Float)
    
    def __repr__(self):
        return f"<Automovel(marca='{self.marca}', modelo='{self.modelo}', ano={self.ano})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'ano': self.ano,
            'motorizacao': self.motorizacao,
            'tipo_combustivel': self.tipo_combustivel,
            'cor': self.cor,
            'quilometragem': self.quilometragem,
            'numero_portas': self.numero_portas,
            'transmissao': self.transmissao,
            'preco': self.preco,
            'potencia': self.potencia,
            'torque': self.torque,
            'capacidade_porta_malas': self.capacidade_porta_malas,
            'consumo_cidade': self.consumo_cidade,
            'consumo_estrada': self.consumo_estrada
        }
