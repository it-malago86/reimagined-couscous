# Usa un'immagine Python leggera
FROM python:3.9-slim

WORKDIR /app

# Copia i requisiti e installa
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice
COPY . .

EXPOSE 5000

CMD ["python", "app/main.py"]
