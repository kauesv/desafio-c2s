import random
import faker
from database.data_source import DatabaseConnection
from models import Automovel


fake = faker.Faker('pt_BR')

MARCAS = [
    "Volkswagen", "Fiat", "Chevrolet", "Ford", "Toyota", "Honda", "Hyundai", 
    "Renault", "Nissan", "Mitsubishi", "Peugeot", "Citroen", "BMW", "Mercedes-Benz", 
    "Audi", "Jeep", "Kia", "Chery", "BYD", "Caoa"
]

MODELOS = {
    "Volkswagen": ["Gol", "Fox", "Polo", "Virtus", "T-Cross", "Nivus", "Taos", "Jetta", "Tiguan"],
    "Fiat": ["Uno", "Argo", "Mobi", "Cronos", "Strada", "Toro", "Pulse", "Fastback"],
    "Chevrolet": ["Onix", "Prisma", "Cruze", "Tracker", "S10", "Spin", "Equinox", "Montana"],
    "Ford": ["Ka", "Fiesta", "Focus", "EcoSport", "Ranger", "Maverick", "Territory", "Bronco"],
    "Toyota": ["Corolla", "Yaris", "Etios", "Hilux", "SW4", "RAV4", "Camry", "Corolla Cross"],
    "Honda": ["Fit", "City", "Civic", "HR-V", "WR-V", "CR-V", "Accord"],
    "Hyundai": ["HB20", "Creta", "Tucson", "ix35", "Santa Fe", "Azera"],
    "Renault": ["Kwid", "Sandero", "Logan", "Stepway", "Duster", "Captur", "Oroch"],
    "Nissan": ["March", "Versa", "Sentra", "Kicks", "Frontier"],
    "Mitsubishi": ["Lancer", "ASX", "Outlander", "Eclipse Cross", "L200 Triton", "Pajero"],
    "Peugeot": ["208", "2008", "3008", "408", "5008"],
    "Citroen": ["C3", "C4 Cactus", "Aircross", "Berlingo", "Jumpy"],
    "BMW": ["Série 1", "Série 3", "X1", "X3", "X5", "320i", "118i", "M3", "M5"],
    "Mercedes-Benz": ["Classe A", "Classe C", "Classe E", "GLA", "GLC", "GLE"],
    "Audi": ["A3", "A4", "A5", "Q3", "Q5", "Q7", "RS5", "TT"],
    "Jeep": ["Renegade", "Compass", "Commander", "Wrangler", "Grand Cherokee"],
    "Kia": ["Picanto", "Rio", "Cerato", "Sportage", "Sorento", "Stinger"],
    "Chery": ["Tiggo 2", "Tiggo 3X", "Tiggo 5X", "Tiggo 7", "Tiggo 8"],
    "BYD": ["Han", "Tang", "Song", "Yuan", "Dolphin", "Seal"],
    "Caoa": ["Chery Tiggo", "Hyundai ix35", "Hyundai New Tucson"]
}

COMBUSTIVEIS = ["Gasolina", "Etanol", "Flex", "Diesel", "Elétrico", "Híbrido"]
CORES = ["Branco", "Preto", "Prata", "Cinza", "Vermelho", "Azul", "Verde", "Amarelo", "Marrom", "Bege"]
TRANSMISSOES = ["Manual", "Automático", "CVT", "Semi-automático", "Automático de dupla embreagem"]


def gerar_automovel():
    """"""
    marca = random.choice(MARCAS)
    modelo = random.choice(MODELOS[marca])
    ano = random.randint(2005, 2025)
    tipo_combustivel = random.choice(COMBUSTIVEIS)

    # Ajustando motorização com base no tipo de carro/combustível
    if tipo_combustivel in ["Elétrico", "Híbrido"]:
        motorizacao = round(random.uniform(1.0, 3.0), 1)
    else:
        motorizacao = round(random.uniform(1.0, 4.0), 1)

    # Cálculo de preço simulado baseado em características
    preco_base = random.randint(20000, 180000)
    fator_ano = (ano - 2005) * 1000
    fator_motor = motorizacao * 10000

    if tipo_combustivel in ["Elétrico", "Híbrido"]:
        fator_combustivel = 30000
    elif tipo_combustivel == "Diesel":
        fator_combustivel = 15000
    else:
        fator_combustivel = 0
        
    preco = preco_base + fator_ano + fator_motor + fator_combustivel
    
    # Quilometragem inversamente proporcional ao ano
    km_max = (2025 - ano) * 20000
    quilometragem = random.randint(100, km_max) if km_max > 100 else 100

    return Automovel(
        marca=marca,
        modelo=modelo,
        ano=ano,
        motorizacao=motorizacao,
        tipo_combustivel=tipo_combustivel,
        cor=random.choice(CORES),
        quilometragem=quilometragem,
        numero_portas=random.choice([2, 4, 5]),
        transmissao=random.choice(TRANSMISSOES),
        preco=preco,
        potencia=random.randint(70, 450),
        torque=round(random.uniform(10.0, 60.0), 1),
        capacidade_porta_malas=random.randint(250, 650),
        consumo_cidade=round(random.uniform(5.0, 15.0), 1),
        consumo_estrada=round(random.uniform(7.0, 18.0), 1)
    )

def popular_banco():
    database = DatabaseConnection()
    
    with database.get_session() as session:
        # Verificando se já existem dados no banco
        count = session.query(Automovel).count()
        if count > 0:
            print(f"O banco de dados já possui {count} registros. Pulando população.")
            return
        
        print("Populando o banco de dados com veículos fictícios...")
        
        # Gerando e inserindo 100 automóveis no banco de dados
        automoveis = [gerar_automovel() for _ in range(100)]
        session.add_all(automoveis)
        session.commit()
        
        print(f"Banco de dados populado com sucesso! {len(automoveis)} veículos inseridos.")

if __name__ == "__main__":
    popular_banco()