# 1. On utilise une image de base Python
FROM python:3.10-slim

# 2. On définit le répertoire de travail dans le conteneur
WORKDIR /app

# 3. On copie les fichiers du projet dans le conteneur
COPY . .

# 4. On installe les dépendances depuis le fichier requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. On expose le port
EXPOSE 5000


# 7. Run the Flask application (dev mode)
CMD ["python", "flask_app/app.py"]
