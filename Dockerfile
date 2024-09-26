# 1. On utilise une image de base Python
FROM python:3.10-slim

# 2. On définit le répertoire de travail dans le conteneur
WORKDIR /app

# 3. On copie les fichiers de ton projet dans le conteneur
COPY . /app

# 4. On copie le fichier requirements.txt
COPY requirements.txt .

# 5. On installe les dépendances depuis le fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 6. On expose le port
EXPOSE 5000

# 7. Commande pour lancer l'application Flask
CMD ["python", "flask_app/app.py"]