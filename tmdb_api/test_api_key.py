import requests
import json
from tmdb_api import api_key

class SearchPerson():
    def __init__(self):
        self.api_key = api_key.api_key
        self.person = input()
        self.url = f"https://api.themoviedb.org/3/search/person?api_key={self.api_key}&query={self.person}"
      
        self.response = requests.get(self.url)
        print(self.response)