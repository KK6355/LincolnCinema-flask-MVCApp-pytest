from flask import Flask,render_template, request
from MovieListDefault import movieListDefault
from ScreenListData import screenList
from SeatListData import seatList
app = Flask(__name__)
@app.route('/')
def index():
    filteredList = movieListDefault
    searchStr = request.args.get('searchStr')
    if searchStr:
        searchStrLower = request.args.get('searchStr').lower()
        filteredList = []
        for movie in movieListDefault:
            index1 = movie.title.lower().find(searchStrLower)
            index2 = movie.genre.lower().find(searchStrLower)
            index3 = movie.language.lower().find(searchStrLower)
            index4 = movie.reDate.lower().find(searchStrLower)
            if index1 != -1 or index2 != -1 or index3 != -1 or index4 != -1:
                filteredList.append(movie)
     
    return render_template('index.html',movieListDefault = filteredList)
@app.route('/movieDetail/<int:movieId>')
def movieDetail(movieId):
    isMovieExisted = False
    movieTitle = ""
    moviePoster = ""
    movieDes = ""
    movieCountry = ""
    movieRuntime = ""
    movieLang = ""
    movieRDate = ""
    movieGenre = ""
    
    for movie in movieListDefault:
        if movie.movieId == movieId:
            isMovieExisted = True
            movieTitle = movie.title
            moviePoster = movie.poster
            movieDes = movie.description
            movieCountry = movie.country
            movieRuntime = movie.runtime
            movieLang = movie.language
            movieRDate = movie.reDate
            movieGenre = movie.genre
    screens = [] 
    seats = seatList  
    #dateList = []
    for screen in screenList:
        if screen.movieId == movieId:
            screens.append(screen)
            
            
            #dateList.append(screen.scheduledDate)
    return render_template('movieDetail.html',movieId=movieId, movieTitle=movieTitle,moviePoster=moviePoster,movieDes=movieDes,
                           movieLang=movieLang,movieRDate=movieRDate,movieCountry=movieCountry,movieRuntime=movieRuntime,movieGenre=movieGenre,isMovieExisted=isMovieExisted,
                           screens=screens,seatList = seats )
