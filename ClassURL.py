import requests

class ClassURL:
    def __init__(self, url):
        self.url = url

    def testUrlValid(self):
        try:
            response = requests.get(self.url)
            return response
        except requests.exceptions.Timeout as e:
            print("La requête a expiré : ", e)
            return None
        except requests.exceptions.ConnectionError as e:
            print("Impossible de se connecter au serveur : ", e)
            return None
        except requests.exceptions.RequestException as e:
            print("Une erreur inconnue s'est produite : ", e)
            return None
