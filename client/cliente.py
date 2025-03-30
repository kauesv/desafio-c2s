from mcp_client import MCPClient
import sys
import time


class AgenteVirtual:

    def __init__(self):
        """Inicializa o agente virtual."""
        self.cliente_mcp = MCPClient()
        self.filtros = {}

    def saudar(self):
        """Exibe saudação inicial do agente."""
        print("Olá! Eu sou seu agente virtual. Como posso ajudar?")
        response = input("Você: ")

        return response

    def despedir(self):
        """Exibe mensagem de despedida."""
        print("Obrigado por utilizar nosso sistema de busca de automóveis!")

    def iniciar(self):
        """Método principal que inicia a interação com o usuário."""
        try:
            # Exibindo saudação inicial
            resposta = self.saudar()

            # Se o usuário indicar que está procurando um veículo, iniciar busca
            if any(termo in resposta.lower() for termo in ['carro', 'automóvel', 'veículo', 'automóveis', 'veículos', 'carros']):
                self.iniciar_busca()
            else:
                print("Atualmente só posso ajudar com busca de automóveis.")
                time.sleep(2)
                self.iniciar()

            # Perguntando se deseja fazer nova busca
            nova_busca = input(
                "Deseja fazer uma nova busca? (s/n)",
                default="n"
            )
            
            if nova_busca.lower() == 's':
                self.filtros = {}
                self.iniciar()
            else:
                self.despedir()
                
        except KeyboardInterrupt:
            print("Busca interrompida pelo usuário.")
            self.despedir()
            sys.exit(0)
        except Exception as e:
            print(f"Erro inesperado: {e}")
            self.despedir()
            sys.exit(1)

    def iniciar_busca(self):
        """Inicia o processo de busca coletando os critérios do usuário."""
        print("Ótimo! Vou ajudá-lo a encontrar o automóvel perfeito para você.")
        print("Vou fazer algumas perguntas para entender melhor o que você está procurando.")
        
        # Coletando os filtros de busca
        self.coletar_filtros()

        # Realizando a busca com os filtros coletados
        self.realizar_busca()

    def coletar_filtros(self):
        """Coleta os critérios de busca do usuário."""
        # Marca
        marca = input("Qual a marca do veículo? (deixe em branco para qualquer marca)")
        if marca.lower() not in ['sair', ''] and len(marca) > 1:
            self.filtros['marca'] = marca
        
        # Modelo (se marca foi especificada)
        if 'marca' in self.filtros:
            modelo = input(f"Qual o modelo {self.filtros['marca']} você procura? (deixe em branco para qualquer modelo)")
            if modelo.lower() not in ['sair', ''] and len(modelo) > 1:
                self.filtros['modelo'] = modelo
        
        # Ano mínimo
        ano_min = input("Qual o ano mínimo do veículo? (deixe em branco para ignorar)")
        if ano_min.lower() not in ['sair', ''] and ano_min.isdigit():
            self.filtros['ano_min'] = int(ano_min)
        
        # Ano máximo
        ano_max = input("Qual o ano máximo do veículo? (deixe em branco para ignorar)")
        if ano_max.lower() not in ['sair', ''] and ano_max.isdigit():
            self.filtros['ano_max'] = int(ano_max)
        
        # Tipo de combustível
        print("Qual tipo de combustível você prefere?")
        print("1. Gasolina")
        print("2. Etanol")
        print("3. Flex")
        print("4. Diesel")
        print("5. Elétrico")
        print("6. Híbrido")
        print("0. Qualquer um")
        
        combustiveis = {
            "1": "Gasolina",
            "2": "Etanol",
            "3": "Flex",
            "4": "Diesel",
            "5": "Elétrico",
            "6": "Híbrido"
        }
        
        tipo_comb = input("Escolha uma opção (0-6): ") or "0"
        if tipo_comb in combustiveis:
            self.filtros['tipo_combustivel'] = combustiveis[tipo_comb]
        
        # Faixa de preço - mínimo
        preco_min = input("Qual o preço mínimo (em R$)? (deixe em branco para ignorar)")
        if preco_min.lower() not in ['sair', ''] and preco_min.replace('.','').isdigit():
            self.filtros['preco_min'] = float(preco_min)
        
        # Faixa de preço - máximo
        preco_max = input("Qual o preço máximo (em R$)? (deixe em branco para ignorar)")
        if preco_max.lower() not in ['sair', ''] and preco_max.replace('.','').isdigit():
            self.filtros['preco_max'] = float(preco_max)
        
        # Cor
        cor = input("Qual a cor que você prefere? (deixe em branco para qualquer cor)")
        if cor.lower() not in ['sair', ''] and len(cor) > 1:
            self.filtros['cor'] = cor
        
        # Número de portas
        portas = input("Quantas portas você prefere? (2, 4 ou 5, deixe em branco para ignorar)")
        if portas.lower() not in ['sair', ''] and portas.isdigit() and int(portas) in [2, 4, 5]:
            self.filtros['numero_portas'] = int(portas)

    def realizar_busca(self):
        """Envia os filtros para o servidor MCP e exibe os resultados."""
        print("Buscando automóveis que atendem aos seus critérios...")

        # Enviar filtros para o servidor MCP
        resposta = self.cliente_mcp.buscar_automoveis(self.filtros)
        
        # Processando resposta
        if resposta['status'] == 'sucesso':
            self.exibir_resultados(resposta)
        else:
            print(f"Erro ao realizar a busca: {resposta.get('mensagem', 'Erro desconhecido')}")

    def exibir_resultados(self, resposta):
        """Exibe os resultados da busca de forma amigável."""
        resultados = resposta.get('resultados', [])
        quantidade = len(resultados)
        
        if quantidade == 0:
            print("Não encontramos automóveis que atendam aos seus critérios.")
            print("Tente novamente com filtros menos específicos.")
            return
        
        print(f"Encontramos {quantidade} automóveis que atendem aos seus critérios!")
        
        # Exibindo cada automóvel
        for i, automovel in enumerate(resultados, 1):
            self.exibir_automovel(automovel)
            
            # Pausar depois de cada 3 automóveis
            if i % 3 == 0 and i < quantidade:
                continuar = input("Pressione ENTER para ver mais resultados ou 'q' para sair.")
                if continuar.lower() == 'q':
                    break

    def exibir_automovel(self, automovel):
        """Exibe os detalhes de um automóvel."""
        painel = f"{automovel['marca']} {automovel['modelo']} {automovel['ano']}\n\n" + \
                f"• Cor: {automovel['cor']}\n" +\
                f"• Motor: {automovel['motorizacao']} ({automovel['tipo_combustivel']})\n" +\
                f"• Quilometragem: {automovel['quilometragem']:,} km\n" +\
                f"• Transmissão: {automovel['transmissao']} ({automovel['numero_portas']} portas)\n" +\
                f"• Potência: {automovel['potencia']} cv\n" +\
                f"• Consumo: {automovel['consumo_cidade']} km/l (cidade) / {automovel['consumo_estrada']} km/l (estrada)\n\n" +\
                f"Preço: R$ {automovel['preco']:,.2f}"
        print(painel)


if __name__ == "__main__":
    agente = AgenteVirtual()
    agente.iniciar()