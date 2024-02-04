from tmdb_api.tmdb_movie import SearchMovie

import json

class MovieDetails():
    def __init__(self):
        self.id_movie = SearchMovie().MovieID()     

    def director(self):
        self.details = self.id_movie
        self.crew = self.details['credits']['crew']

        for dir in range(len(self.crew)):
            if self.crew[dir]['job'] == 'Director':
                self.director_id = self.crew[dir]['id']
                self.director_name = self.crew[dir]['name']
        
        return [self.director_id, self.director_name]

    def top_cast(self):
        self.details = self.id_movie
        self.cast = self.details['credits']['cast']
        self.topCast = []
        for cast in range(len(self.cast)):
            self.actor = self.cast[cast]['name']
            self.topCast.append(self.actor)
            if cast > 5:
                break
        return self.topCast
        
    def genres_id(self):
        self.details = self.id_movie
        self.genres = self.details['genres']
        
        self.genreList = []
        for genres in self.genres:
            self.gen = genres['name']
            self.id_gen = genres['id']
            self.genreList.append({'id': self.id_gen, 'name': self.gen})
            
        return self.genreList
    
    def _keywords(self):
        self.details = self.id_movie
        self.keyword = self.details['keywords']
        self.keyList = []
        for keywords in self.keyword['keywords']:
           self.words = keywords['name']
           self.keyList.append(self.words)
        
        return self.keyList
        #for loop generos
           
    def _similiar_details(self):
        self.details = self.id_movie
        self.recom = self.details ['similar']['results']
        
        self.similarMovie = []


        for i in range(len(self.recom)):
            self.id = self.recom[i]['id']
            self.gen_ids = self.recom[i]['genre_ids'], 
            self.title = self.recom[i]['title'], 
            self.date = self.recom[i]['release_date']
            self.overview = self.recom[i]['overview']
            self.similarMovie.append({'id':self.id, 'title':self.title[0], 'date':self.date, 'genre':self.gen_ids[-1], 'overview':self.overview})
        
        self.jsSimiliar = json.dumps(self.similarMovie, indent=4)
        
        return self.jsSimiliar

    def _recon_details(self):
        self.details = self.id_movie
        self.recom = self.details['recommendations']['results']
        
        self.recomMovie = []


        for i in range(len(self.recom)):
            self.id = self.recom[i]['id']
            self.gen_ids = self.recom[i]['genre_ids'], 
            self.title = self.recom[i]['title'], 
            self.date = self.recom[i]['release_date']
            self.overview = self.recom[i]['overview']
            self.recomMovie.append({'id':self.id, 'title':self.title[0], 'date':self.date, 'genre':self.gen_ids[-1], 'overview':self.overview})
        self.jsRecon = json.dumps(self.recomMovie, indent=4)
        
        return self.jsRecon
    
    def providers(self):
        self.view = f"Não está disponível para streaming, aluguel ou compra"
        self.details = self.id_movie
        try:
            self.watchers = self.details['watch/providers']['results']['BR']
        except:
            self.view = f'Não se encontra disponivel no Brasil em nenhuma plataforma.'
            return self.view
       
        for watch in self.watchers:
           
            if watch == 'flatrate':
                self.view = f"Disponível em: {self.watchers[watch][0]['provider_name']}"
            if watch == 'rent':
                self.view = f'Disponível para alugar em: {self.watchers[watch][0]["provider_name"]}'
            if watch == 'buy':
                self.view = f'Disponível para comprar em: {self.watchers[watch][0]["provider_name"]}'
    
        return self.view


    def movie_details(self):
        self.title = self.id_movie['title']
        self.id_mov = self.id_movie['id']
        self.date = self.id_movie['release_date'][0:4]
        self.dirName = self.director()[1]
        self.cast = self.top_cast()[0:5]
        self.genre = self.genres_id()[0]['name']
        self.overview = self.id_movie['overview']
        self.watch = self.providers()

        return f'\nTitulo: {self.title}\nDiretor: {self.dirName}\nAno: {self.date}\nGeneros: {self.genre}\nElenco: {self.cast}\nSinopse: {self.overview}\n{self.watch}\nAs informações sobre streaming, aluguel e compra do filme é fornecida por JustWatch.'
