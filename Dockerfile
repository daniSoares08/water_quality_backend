# Usa uma imagem Python leve
FROM python:3.11-slim

# Define a pasta de trabalho no container
WORKDIR /app

# Copia requirements primeiro (pra otimizar cache)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o projeto (exceto o que tiver no .dockerignore)
COPY . .

# Expõe a porta 5000
EXPOSE 5000

# Comando padrão para rodar o app com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
