#!/bin/bash

# Se não existir o arquivo de banco, cria
if [ ! -f "/app/data/sensors.db" ]; then
  echo "Nenhum sensors.db encontrado. Criando novo a partir de create_db.sql..."
  sqlite3 /app/data/sensors.db < /app/create_db.sql
else
  echo "Banco sensors.db já existe. Não é necessária a criação"
fi

# Agora executa o comando (Gunicorn ou Python) que vem lá no CMD
exec "$@"
