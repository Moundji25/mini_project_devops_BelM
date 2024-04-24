from flask import Flask
app = Flask(__name__)

# Définir une liste de membres
list_of_members = ['Moses Eyong', 'Junior KAMSAP', 'seydina diame']

@app.route("/")
def afficher_les_membres():
    membres = "<h1>Membres de l'équipe :</h1>"
    for membre in list_of_members:
        membres += f"<p>{membre}</p>"
    return membres

# Exécuter l'application Flask
if __name__ == "__main__":
    app.run(debug=True)
