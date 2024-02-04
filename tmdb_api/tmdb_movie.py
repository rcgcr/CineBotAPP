import requests
from tmdb_api.api_key import api_key


class SearchMovie():
    def __init__(self):
        self.api_key = api_key
        self.movie = input("Filme: ")
        self.year = input("Ano: ")
        
        self.url = f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}&query={self.movie}&year={self.year}&language=pt-BR"
        self.response = requests.get(self.url)
        self.movie = self.response.json()
        self.id = self.movie['results'][0]['id']
    
    def MovieID(self):
        self.url = f"https://api.themoviedb.org/3/movie/{self.id}?api_key={self.api_key}&append_to_response=credits,keywords,similar,recommendations,watch/providers&language=pt-BR"
        self.response = requests.get(self.url)
        self.movie_id = self.response.json()
        return self.movie_id



        




