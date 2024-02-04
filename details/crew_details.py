from tmdb_api.tmdb_director import SearchPerson
from details.movie_details import MovieDetails
import json
import random

class CrewDetails():
    def __init__(self):
        self.id_crew = SearchPerson().PersonID()
        
    def credits_combined(self):
        
        self.credits = self.id_crew
        
       
        self.movieCredits = []
        self.tvCredits = []
        for media in self.credits['crew']:
            if media['media_type'] == 'movie':
                self.movieTitle = media['title']
                self.genre = media['genre_ids']
                self.movieJob = media['job']
                self.movieOverview = media['overview']
                self.releaseDate =media['release_date']
                self.movieCredits.append({'media':'Movie', 'title':self.movieTitle,'year':self.releaseDate, 'genres': self.genre, 'job':self.movieJob})

            if media['media_type'] == 'tv':
                self.tvTitle = media['name']
                self.genre = media['genre_ids']
                self.tvJob = media['job']
                self.tvOverview = media['overview']
                self.tvCredits.append({'media': 'TV', 'title':self.tvTitle,'genres':self.genre, 'job':self.tvJob})
        
        return self.movieCredits
    
    def matches(self):
        self.credits = self.credits_combined()
        self.credits_title = []
        for i in range(len(self.credits)):
            self.credits_title.append((self.credits[i]['title'], self.credits[i]['year'], self.credits[i]['job']))
        
        return self.credits_title
        
    def detailed_matches(self):
        self.selected = random.choices(self.matches(), k=5)
        print()
        print("os filmes indicado são: ","\n")
        self.movies = [print(movies[0], "Ano:", movies[1][0:4], "-Função:", movies[2]) for movies in set(self.selected)]
        print()
        print("Para saber mais sobre um filme da lista. Ou outro filme de seu interesse.Digite o nome do filme: ", "\n")
        self.movie = MovieDetails().movie_details()
        print(self.movie,'\n')
        print()
        
