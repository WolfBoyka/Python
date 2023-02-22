import sys
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Récupération de l'adresse du site à générer en paramètre
siteAddress = ""
try:
    if len(sys.argv) > 1:
        siteAddress = sys.argv[1]
except:
    print("Aucun parametre n'a ete fourni.")

# Lit le contenu du template et remplace la variable {{ siteToGenerate }}
with open('templates/template.html', 'r') as f:
    content = f.read().replace('{{ siteToGenerate }}', siteAddress)

# Écrit le contenu modifié dans un nouveau fichier avec le nom siteAddress.html
with open(f'templates/{siteAddress}', 'w') as f:
    f.write(content)