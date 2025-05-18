# Etapa base: imagem Python
FROM python:3.12-slim

WORKDIR /app

# Copiar requirements primeiro para aproveitar cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Criar diretórios necessários e definir permissões
RUN mkdir -p /app/data/raw /app/data/processed /app/models/trained \
    && chmod -R 777 /app/data /app/models

# Copiar o código-fonte
COPY src/ ./src/

# Adicionar o diretório atual ao PYTHONPATH
ENV PYTHONPATH=/app

# Executar o script principal
CMD ["python", "src/insert_weather.py"]