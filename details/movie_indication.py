
from details.movie_details import MovieDetails

import random
import json

class Indications:
    def __init__(self):
        self.movie = MovieDetails()
        self.genre =self.movie.genres_id()
        self.keywords = self.movie._keywords()
        self.recom = self.movie._recon_details()
        self.similar = self.movie._similiar_details()
        
    
    def id_movie(self):
        self.gen_id = []
        self.gen_name = []
        for id_movie in range(len(self.genre)):
            self.gen_id.append(self.genre[id_movie]['id'])
            self.gen_name.append(self.genre[id_movie]['name'])
            
        return self.gen_id
    
    def similar_indications(self):
        self.jsRecon = json.loads(self.similar)
        self.id_genre = self.id_movie()
        self.keys = set(self.keywords)
        self.similar_match = []

        for movies in range(len(self.jsRecon)):
            self.wrds = self.jsRecon[movies]['overview'].split(" ")
            self.wrds_set = set(self.wrds)
            self.id_set = set(self.jsRecon[movies]['genre'])
           
          
            self.difference = self.wrds_set.intersection(self.keys)
            
            
            
            if self.difference:
                self.sim_match = self.jsRecon[movies]['title']
                self.similar_match.append(self.sim_match)
                
            
            self.id_inter = self.id_set.intersection(self.id_genre)
            if self.id_inter:
                if len(self.id_inter) == len(self.id_genre):
                    self.id_match = self.jsRecon[movies]['title']
                    self.similar_match.append(self.id_match)
                    #print(self.id_match)
                else:
                    for movie in range(len(self.jsRecon)):
                        self.similar_match.append((self.jsRecon[movie]['title'],self.jsRecon[movie]['date']))
        
        return self.similar_match
   
    def recom_indications(self):
        self.jsRecon = json.loads(self.recom)
        self.id_genre = self.id_movie()
        self.keys = set(self.keywords)
        
        self.wrds_overview = {}
        self.recom_match = []
        
        for movies in range(len(self.jsRecon)):

            self.wrds = self.jsRecon[movies]['overview'].split(" ")
            self.wrds_set = set(self.wrds)
            self.id_set = set(self.jsRecon[movies]['genre'])
           
            
            self.difference = self.wrds_set.intersection(self.keys)            
            if self.difference:
                self.dif_match = self.jsRecon[movies]['title']
                self.recom_match.append(self.dif_match)
                #print(self.dif_match, self.difference)
            
            self.id_inter = self.id_set.intersection(self.id_genre)
            if self.id_inter:
                if len(self.id_inter) == len(self.id_genre):
                   self.id_match = self.jsRecon[movies]['title']
                   self.recom_match.append(self.id_match)
                   #print(self.id_match, self.id_inter)
                else:
                    for movie in range(len(self.jsRecon)):
                        self.recom_match.append((self.jsRecon[movie]['title'],self.jsRecon[movie]['date']))
        
        return self.recom_match

    def matches(self):
        self.recomMatch = self.recom_indications()
        self.simMatch = self.similar_indications()
        self.MatchAll = self.recomMatch + self.simMatch
        
        return self.MatchAll

    def detailed_match(self):
        self.selected = random.choices(self.matches(), k=5)
        
        print("os filmes indicado são: ","\n")
        self.movies = [print(movies[0], "ano:", movies[1][0:4]) for movies in set(self.selected)]
        print()
        print("Para saber mais sobre um filme da lista. Ou outro filme de seu interesse.Digite o nome do filme: ", "\n")
        self.movie = MovieDetails().movie_details()
        print(self.movie,'\n')
        print()
        
     
    
        
        
        
       

        

        
        



            

        
                           
    