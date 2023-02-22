import requests
import datetime
import sys
import ClassAlerte

# script de check de code html
siteToRequest = input("Entrez le site que vous souhaitez tester : ")
urlCompleted = "http://" + siteToRequest
print("Vous souhaitez tester le site : " + urlCompleted)

try:
    
    urlRedirect = requests.get(urlCompleted, allow_redirects=True)
    if urlRedirect.history:
        print("La requete a ete redirigee.")
        for r in urlRedirect.history:
            print("Code retour : " + str(r.status_code))
        print("La nouvelle destination est :", urlRedirect.url)
        urlToVerify = requests.head(str(urlRedirect.url))
    else:
        print("La requete n'a pas ete redirigee.")
        urlToVerify = requests.head(urlCompleted)

except Exception as error:
    print("Erreur lors de la verification de : " + urlCompleted + " => ", error)
    print("L'url donnee est invalide !")
    sys.exit(1)

print("Teste du site : " + urlToVerify.url)

maintenant = datetime.datetime.now()

with open("Results\\result.txt", 'a') as f:
    f.write("\n" + str(maintenant) + " | Code retour du site : " + urlToVerify.url + " : " + str(urlToVerify.status_code))

alerte = ClassAlerte()
if alerte.getAlerte(urlToVerify) == 200:

    urlVerified = requests.get(urlToVerify.url)
    with open("Results\\result.txt", 'a') as f:
        f.write("\nCode retour OK")

else : 
    with open("Results\\result.txt", 'a') as f:
        f.write("\nCode retour KO")