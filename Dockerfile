FROM python:3.12-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro para aproveitar cache do Docker
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar o resto da aplicação
COPY . .

# Expor a porta (com fallback para 5000)
EXPOSE ${PORT:-5000}

# Comando para executar a aplicação
CMD gunicorn app:app --bind 0.0.0.0:${PORT:-5000} --workers 1 --timeout 120 