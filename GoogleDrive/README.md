# TELECHARGER DANS LE DRIVE L'IMAGE ADEQUAT
1. Dans google colab, aller sur le fichier SentenceTransform.ipynb
2. Lancer la requête :
search("exemple", "phrase à illustrer(en anglais)")

ex : search("chiens","dogs playing in the snow")

3. L'image se télécharge dans le drive lié

# RAJOUTER L'IMAGE A MONTRER DEPUIS LE DRIVE
1. Dans le file quickstart.py modifier l'argument ligne 61 par l'example
if __name__ == '__main__':
    main("example")
2. L'image apparaît dans static/IMG

# LANCER L"APP FLASK
1. On se place dans le bon directory:
cd GoogleDrive/

2. On explicite les variables d'environnement propres à FLASK :
export FLASK_APP=index
export FLASK_ENV= devlopment

3. On lance le serveur
flask run

