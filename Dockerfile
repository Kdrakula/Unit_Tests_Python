# Dockerfile.builder
FROM python:3.11

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie całego repozytorium do obrazu
COPY . /app

# Instalacja zależności, jeśli istnieje plik requirements.txt
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Uruchomienie testów jednostkowych
CMD ["python", "-m", "unittest", "discover", "tests"]
