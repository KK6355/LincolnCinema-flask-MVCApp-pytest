import requests
class Movie:
    """! The Movie class
    Defines class for movies
    """
    nextId = 4000
    APIKey = '1015babb'
    
    def __init__(self,title,language,genre,reDate):
        self.__movieId = Movie.nextId
        self.__title = title
        self.__language = language
        self.__genre = genre
        self.__reDate = reDate
        Movie.nextId += 1
        self.movieTimes = []
        self.data = requests.get(f'http://www.omdbapi.com/?t={self.title}&apikey={self.APIKey}').json()
        
    @property
    def movieId(self):
        return self.__movieId
    @property
    def title(self):
        return self.__title
    @property
    def language(self):
        return self.__language
    @property
    def genre(self):
        return self.__genre
    @property
    def reDate(self):
        return self.__reDate
    @property
    def poster(self): 
        return self.data["Poster"]      
    @property
    def country(self): 
        return self.data["Country"]
    @property
    def runtime(self): 
        return self.data["Runtime"]
    @property
    def description(self): 
        return self.data["Plot"]    

    
    def info(self):
        print(f"Movie Id:{self.movieId},title:{self.title}, language:{self.language}, genre:{self.genre}, released date:{self.reDate}")