import datetime
from ClassURL import ClassURL
import sys
import os

dateTimeNow = datetime.datetime.now()

# Récupération du site à générer en paramètre
siteToRequest = ""
try:
    print(sys.argv)
    if len(sys.argv) > 1:
        siteToRequest = sys.argv[1]
except:
    print("Aucun parametre n'a ete fourni.")

# Ajouter le préfixe "http://" au site à générer pour construire le nom du fichier HTML
siteToGenerate = f"http://{siteToRequest}"
siteHTML = f"{siteToGenerate}.html"
print(siteHTML)

# Appel du script de génération de site
os.system(f'python GenerateWebSite.py {siteHTML}')

# Vérification de l'existence du fichier HTML généré
if os.path.exists(siteHTML):
    # Initialisation de l'objet ClassURL
    objectURL = ClassURL(siteHTML)

    # Vérification de l'existence de l'URL
    urlVerified = objectURL.testUrlValid()

    if urlVerified:
        # Ouverture du fichier HTML dans le navigateur par défaut
        os.startfile('templates/' + urlVerified.url)

        # Ecriture dans le log resultURL.log
        logURL = "Results\\resultURL.log"
        with open(logURL, 'a') as f:
            if f.tell() != 0:  # Vérifie si le fichier n'est pas vide
                f.write("\n")
            f.write(str(dateTimeNow) + " | Code retour du site : " + urlVerified.url + " = " + str(urlVerified.status_code))

        if urlVerified.status_code == 200:
            with open(logURL, 'a') as f:
                f.write(" | Code retour OK")
        else:
            with open(logURL, 'a') as f:
                f.write(" | Code retour KO")
    else:
        print("Impossible de verifier l'URL")
else:
    print(f"Le fichier {siteHTML} n'a pas ete genere")
