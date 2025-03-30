from config import Config
import websockets
import json


class MCPClient:
    """
    Cliente para comunicação com o servidor MCP (Model Context Protocol).
    Esta classe gerencia a conexão WebSocket e envia/recebe mensagens do servidor.
    """
    
    def __init__(self, host=Config.HOST_SERVER, port=Config.PORT_SERVER):
        """
        Inicializa o cliente MCP.
        
        Args:
            host (str): O endereço do host do servidor MCP
            port (int): A porta do servidor MCP
        """
        self.uri = f"ws://{host}:{port}"
    
    async def enviar_filtros(self, filtros):
        """
        Envia filtros de busca para o servidor MCP e retorna os resultados.
        
        Args:
            filtros (dict): Um dicionário com os filtros de busca
            
        Returns:
            dict: A resposta do servidor contendo os resultados da busca
        """
        try:
            # Conectando ao servidor MCP
            print(f"Conectando ao servidor MCP em {self.uri}...")
            async with websockets.connect(self.uri) as websocket:
                # Construindo a mensagem com os filtros
                mensagem = {
                    'filtros': filtros
                }
                
                # Convertendo para JSON e enviando para o servidor
                await websocket.send(json.dumps(mensagem))
                print(f"Filtros enviados: {filtros}")
                
                # Aguardando a resposta do servidor
                resposta = await websocket.recv()
                resposta_dict = json.loads(resposta)
                
                return resposta_dict
                
        except websockets.exceptions.ConnectionRefused:
            print(f"Não foi possível conectar ao servidor MCP em {self.uri}")
            return {
                'status': 'erro',
                'mensagem': f'Falha na conexão com o servidor em {self.uri}.',
                'resultados': []
            }
        except Exception as e:
            print(f"Erro ao comunicar com o servidor: {e}")
            return {
                'status': 'erro',
                'mensagem': f'Erro na comunicação: {str(e)}',
                'resultados': []
            }