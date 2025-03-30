#!/bin/bash
echo "Configurando ambiente virtual para o projeto de busca de automóveis..."

# Verificando se python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "python3 não foi encontrado! Por favor, instale python 3.9+ e tente novamente."
    exit 1
fi

# Verificando se venv está instalado
if ! python3 -c "import venv" &> /dev/null; then
    echo "Módulo venv não encontrado. Instalando..."
    python3 -m pip install venv
fi

# Criando diretório para ambientes virtuais se não existir
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual para o projeto..."
    python3 -m venv venv
else
    echo "Ambiente virtual já existe."
fi

# Ativando o ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Falha ao ativar o ambiente virtual."
    exit 1
fi
echo "Ambiente virtual ativado com sucesso."

echo "Atualizando pip..."
python3 -m pip install --upgrade pip

echo "Instalando dependências do servidor..."
cd server
pip install -r requirements.txt --no-cache-dir
cd ..

echo "Instalando dependências do cliente..."
cd client
pip install -r requirements.txt --no-cache-dir
cd ..

echo
echo "======================================================="
echo "Ambiente virtual configurado com sucesso!"
echo
echo "Para iniciar o servidor: ./run_server.sh"
echo "Para iniciar o cliente: ./run_client.sh"
echo "======================================================="

exit 0
