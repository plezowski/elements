FROM python:3

# copie les fichiers dans le conteneur
COPY . /usr/src/
# règle le répertoire de travail
WORKDIR /usr/src/flask

# installe les bibliothèques requises
RUN pip install --no-cache-dir colorama markdown Flask

# exécute la commande pour créer le fichier markdown
RUN cd .. && python classifier.py flask/liste.md

# il faut exposer un port
EXPOSE 5000

# exécute la commande (éventuellement avec un paramètre)
ENTRYPOINT [ "python", "./app.py" ]
CMD ["tout le monde"]