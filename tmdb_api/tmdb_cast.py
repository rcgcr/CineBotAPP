import requests
import json
from tmdb_api import api_key


class SearchPerson():
    def __init__(self):
        self.api_key = api_key.api_key
        self.person = input("Ator/Atriz: ")
        self.url = f"https://api.themoviedb.org/3/search/person?api_key={self.api_key}&query={self.person}&language=pt-BR"
        self.response = requests.get(self.url)
        self.cast = self.response.json()
        self.id = self.cast['results'][0]['id']
    
    def PersonID(self):
        
        self.url = f"https://api.themoviedb.org/3/person/{self.id}/combined_credits?api_key={self.api_key}&language=pt-BR"
   
        self.response = requests.get(self.url)
        self.credits = self.response.json()
        return self.credits
    
   

