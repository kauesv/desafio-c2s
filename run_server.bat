@echo off
echo Iniciando servidor MCP de busca de automóveis...

:: Verificando se o ambiente virtual existe
if not exist "venv\" (
    echo Ambiente virtual não encontrado! Execute setup_venv.bat primeiro.
    exit /b 1
)

:: Ativando o ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate.bat
if %ERRORLEVEL% NEQ 0 (
    echo Falha ao ativar o ambiente virtual.
    exit /b 1
)
echo Ambiente virtual ativado com sucesso.

:: Iniciando o servidor
cd server
python app.py