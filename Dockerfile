# Usa Python 3.11 com imagem leve
FROM python:3.11-slim

# Atualiza e instala o sqlite3
RUN apt-get update && apt-get install -y sqlite3

# Cria pasta de trabalho
WORKDIR /app

# Copia o requirements e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto
COPY . .

# Dá permissão pro entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expõe a porta 5000
EXPOSE 5000

# Primeiro roda o entrypoint.sh e depois o CMD
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
