import requests
url_base = "https://hp-api.onrender.com/api"
response = requests.get(url=f"{url_base}/characters")
print(response)

class hpAPI():
    def __init__(self):
        print("Objeto creado")
        self.__url_base = "https://hp-api.onrender.com/api"

    def personajes(self):
        import requests
        response = requests.get(f"{self.__url_base}/characters")
        return response.json()
    
    def hechizos(self):
        import requests
        response = requests.get(f"{self.__url_base}/spells")
        return response.json()

    def personaje_por_casa(self, casa):
        import requests
        response = requests.get(f"{self.__url_base}/characters/house/{casa}")
        return response.json()
    
harry_api = hpAPI()
print(harry_api.personaje_por_casa('gryffindor'))
