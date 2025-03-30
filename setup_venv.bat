@echo off
echo Configurando ambiente virtual para o projeto de busca de automóveis...

:: Verificando se py está instalado
where py >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo py não foi encontrado! Por favor, instale py 3.9+ e tente novamente.
    exit /b 1
)

:: Criando diretório para ambientes virtuais se não existir
if not exist "venv\" (
    echo Criando ambiente virtual para o projeto...
    py -m venv venv
) else (
    echo Ambiente virtual já existe.
)

:: Ativando o ambiente virtual
echo Ativando ambiente virtual...
call venv\Scripts\activate
if %ERRORLEVEL% NEQ 0 (
    echo Falha ao ativar o ambiente virtual.
    exit /b 1
)
echo Ambiente virtual ativado com sucesso.

echo Atualizando pip...
py -m pip install --upgrade pip

echo Instalando dependências do servidor...
cd server
pip install -r requirements.txt --no-cache-dir
cd ..

echo Instalando dependências do cliente...
cd client
pip install -r requirements.txt --no-cache-dir
cd ..

echo.
echo =======================================================
echo Ambiente virtual configurado com sucesso!
echo.
echo Para iniciar o servidor: .\run_server.bat
echo Para iniciar o cliente: .\run_client.bat
echo =======================================================

exit /b 0

call venv\Scripts\activate