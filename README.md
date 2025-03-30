## Descrição

Proposto pela empresa [C2S](https://www.contact2sale.com/), estes desafios visam avaliar tecnicamente os candidatos ao processo seletivo para a vaga de **Desenvolvedor Python**.

## Projeto

Este projeto implementa um sistema de consulta de automóveis composto por:

1. **Servidor MCP**: API para consulta de automóveis em um banco de dados SQLite
2. **Cliente MCP**: Interface de linha de comando interativa com um agente virtual para auxiliar na busca de automóveis

O sistema permite buscar veículos baseados em diversos critérios como marca, modelo, ano, tipo de combustível, preço, cor e número de portas.

## Estrutura do Projeto

```
desafio-c2s/
├── client/                 # Código do cliente
│   ├── cliente.py          # Interface do agente virtual
│   ├── config.py           # Configurações do cliente
│   ├── mcp_client.py       # Implementação do protocolo MCP
│   └── requirements.txt    # Dependências do cliente
├── server/                 # Código do servidor
│   ├── app.py              # Aplicação principal do servidor
│   ├── config.py           # Configurações do servidor
│   ├── mcp_server.py       # Implementação do protocolo MCP
│   ├── models.py           # Modelos de dados SQLAlchemy
│   ├── requirements.txt    # Dependências do servidor
│   ├── data/               # Diretório para armazenamento de dados
│   │   └── database.db     # Banco de dados SQLite
│   ├── database/           # Camada de acesso a dados
│   │   ├── __init__.py
│   │   └── data_source.py  # Conexão com o banco de dados
│   └── utils/              # Utilitários
│       └── database/       # Utilitários para banco de dados
│           ├── __init__.py
│           └── seed_vehicles.py  # Geração de dados iniciais
├── run_client.bat          # Script para executar o cliente (Windows)
├── run_client.sh           # Script para executar o cliente (Linux/Mac)
├── run_server.bat          # Script para executar o servidor (Windows)
├── run_server.sh           # Script para executar o servidor (Linux/Mac)
├── setup_venv.bat          # Script para configurar ambiente virtual (Windows)
└── setup_venv.sh           # Script para configurar ambiente virtual (Linux/Mac)
```

## Instalação e Configuração

### Windows

1. Execute o script `setup_venv.bat` para configurar os ambientes virtuais para cliente e servidor:
   ```
   setup_venv.bat
   ```

2. Ative a Venv:
   ```
   venv\scripts\activate
   ```

3. Inicie o servidor:
   ```
   run_server.bat
   ```

4. Em outro terminal, inicie o cliente:
   ```
   run_client.bat
   ```

### Linux/Mac

1. Torne os scripts executáveis:
   ```
   chmod +x *.sh
   ```

2. Execute o script de configuração:
   ```
   ./setup_venv.sh
   ```

3. Ative a Venv:
   ```
   venv/bin/activate
   ```

4. Inicie o servidor:
   ```
   ./run_server.sh
   ```

5. Em outro terminal, inicie o cliente:
   ```
   ./run_client.sh
   ```

## Utilizando o Sistema

1. Após iniciar o cliente, interaja com o agente virtual
2. Responda às perguntas sobre o automóvel que deseja encontrar
3. Visualize os resultados formatados exibidos na tela
4. Você pode iniciar uma nova busca ou sair do sistema

## Arquitetura

O sistema utiliza uma arquitetura cliente-servidor com comunicação via protocolo MCP (Model Context Protocol):

1. **Servidor**: 
   - Implementa um serviço de consulta a um banco de dados SQLite
   - Processa requisições de busca com base nos filtros recebidos
   - Retorna resultados formatados para o cliente

2. **Cliente**:
   - Interface de linha de comando com estilo conversacional
   - Agente virtual que guia o usuário na definição dos critérios de busca
   - Exibe os resultados de forma formatada e amigável

## Contato

Para mais informações ou para discutir qualquer um dos repositórios, sinta-se à vontade para entrar em contato:

- **Email:** [kauesousavieira534@gmail.com](mailto:kauesousavieira534@gmail.com)
- **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/kaue-sousa-vieira/)

---
Obrigado por visitar meu repositório!