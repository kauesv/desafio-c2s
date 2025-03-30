from database.data_source import DatabaseConnection
from models import Automovel
from sqlalchemy import and_
from config import Config
import websockets
import asyncio
import json


class MCPServer:
    def __init__(self, host=Config.HOST_SERVER, port=Config.PORT_SERVER):
        self.host = host
        self.port = port
        self.database = DatabaseConnection()
    
    async def processar_filtros(self, filtros):
        """
        Processa os filtros recebidos e consulta o banco de dados
        para encontrar automóveis que correspondam aos critérios.
        """
        print(f"Processando filtros: {filtros}")
        
        # Construindo as condições para a consulta
        condicoes = []
        
        # Filtragem por marca
        if 'marca' in filtros and filtros['marca']:
            condicoes.append(Automovel.marca == filtros['marca'])
        
        # Filtragem por modelo
        if 'modelo' in filtros and filtros['modelo']:
            condicoes.append(Automovel.modelo == filtros['modelo'])
        
        # Filtragem por ano mínimo
        if 'ano_min' in filtros and filtros['ano_min']:
            condicoes.append(Automovel.ano >= filtros['ano_min'])
        
        # Filtragem por ano máximo
        if 'ano_max' in filtros and filtros['ano_max']:
            condicoes.append(Automovel.ano <= filtros['ano_max'])
        
        # Filtragem por tipo de combustível
        if 'tipo_combustivel' in filtros and filtros['tipo_combustivel']:
            condicoes.append(Automovel.tipo_combustivel == filtros['tipo_combustivel'])
        
        # Filtragem por preço mínimo
        if 'preco_min' in filtros and filtros['preco_min']:
            condicoes.append(Automovel.preco >= filtros['preco_min'])
        
        # Filtragem por preço máximo
        if 'preco_max' in filtros and filtros['preco_max']:
            condicoes.append(Automovel.preco <= filtros['preco_max'])
        
        # Filtragem por cor
        if 'cor' in filtros and filtros['cor']:
            condicoes.append(Automovel.cor == filtros['cor'])
        
        # Filtragem por transmissão
        if 'transmissao' in filtros and filtros['transmissao']:
            condicoes.append(Automovel.transmissao == filtros['transmissao'])
        
        # Filtragem por número de portas
        if 'numero_portas' in filtros and filtros['numero_portas']:
            condicoes.append(Automovel.numero_portas == filtros['numero_portas'])
        
        # Executando a consulta
        session = self.database.get_session()
        if condicoes:
            query = session.query(Automovel).filter(and_(*condicoes))
        else:
            query = session.query(Automovel)
        
        # Limitando resultados para não sobrecarregar
        automoveis = query.limit(20).all()
        
        # Convertendo os resultados para dicionários
        resultados = [automovel.to_dict() for automovel in automoveis]
        
        return resultados
    
    async def manipular_conexao(self, websocket):
        """Manipula uma conexão websocket com um cliente."""
        try:
            print(f"Nova conexão estabelecida: {websocket.remote_address}")
            
            # Recebendo a mensagem do cliente
            mensagem = await websocket.recv()
            print(f"Mensagem recebida: {mensagem}")
            
            # Convertendo a mensagem JSON para um dicionário Python
            try:
                dados = json.loads(mensagem)
                
                # Verificando se a mensagem contém filtros
                if 'filtros' in dados:
                    filtros = dados['filtros']
                    
                    # Processando os filtros e consultando o banco de dados
                    resultados = await self.processar_filtros(filtros)
                    
                    # Enviando os resultados de volta para o cliente
                    await websocket.send(json.dumps({
                        'status': 'sucesso',
                        'resultados': resultados,
                        'quantidade': len(resultados)
                    }))
                    
                else:
                    await websocket.send(json.dumps({
                        'status': 'erro',
                        'mensagem': 'Formato de mensagem inválido. É necessário fornecer filtros.'
                    }))
                    
            except json.JSONDecodeError:
                await websocket.send(json.dumps({
                    'status': 'erro',
                    'mensagem': 'Formato JSON inválido.'
                }))
                
        except websockets.exceptions.ConnectionClosed:
            print(f"Conexão fechada: {websocket.remote_address}")
        
        except Exception as e:
            print(f"Erro ao manipular conexão: {e}")
            try:
                await websocket.send(json.dumps({
                    'status': 'erro',
                    'mensagem': f'Erro no servidor: {str(e)}'
                }))
            except:
                pass
    
    async def iniciar_servidor(self):
        """Inicia o servidor websocket."""
        try:
            server = await websockets.serve(
                self.manipular_conexao,
                self.host,
                self.port
            )
            print(f"Servidor MCP iniciado em ws://{self.host}:{self.port}")
            
            # Mantém o servidor rodando indefinidamente
            await server.wait_closed()
            
        except Exception as e:
            print(f"Erro ao iniciar o servidor: {e}")
    
    def iniciar(self):
        """Método auxiliar para iniciar o servidor de forma síncrona."""
        asyncio.run(self.iniciar_servidor())