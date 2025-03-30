#!/bin/bash
echo "Iniciando cliente de busca de automóveis..."

# Verificando se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "Ambiente virtual não encontrado! Execute setup_venv.sh primeiro."
    exit 1
fi

# Ativando o ambiente virtual
echo "Ativando ambiente virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Falha ao ativar o ambiente virtual."
    exit 1
fi
echo "Ambiente virtual ativado com sucesso."

# Iniciando o cliente
cd client
python app.py
