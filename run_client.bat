@echo off
echo Iniciando cliente de busca de automóveis...

:: Verificando se o ambiente virtual existe
if not exist "venv\" (
    echo Ambiente virtual não encontrado! Execute setup_venv.bat primeiro.
    exit /b 1
)

:: Ativando o ambiente virtual
call venv\Scripts\activate

:: Verificando se as dependências estão instaladas
python -c "import rich" 2>NUL
if %ERRORLEVEL% NEQ 0 (
    echo Dependência não encontrada: rich
    echo Instalando dependências necessárias...
    cd client
    pip install rich websockets colorama prompt_toolkit --no-cache-dir
    cd ..
)

:: Configurando variáveis de ambiente para o cliente
set MCP_HOST=localhost
set MCP_PORT=8765

:: Iniciando o cliente
cd client
python cliente.py