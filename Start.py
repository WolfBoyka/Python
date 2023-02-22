import datetime
from ClassURL import ClassURL
import requests

dateTimeNow = datetime.datetime.now()

# Initialisation de l'objet ClassURL
siteToRequest = input("Entrez le site que vous souhaitez tester : ")
urlCompleted = "http://" + siteToRequest
objectURL = ClassURL(urlCompleted)

# Vérification de l'existence de l'URL
urlVerified = objectURL.testUrlValid()

if urlVerified:
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
    print("Impossible de vérifier l'URL.")
