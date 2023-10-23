from flask import Flask,render_template, request
from MovieListDefault import movieListDefault
app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template('index.html',movieListDefault = movieListDefault)
@app.route('/movieDetail/<int:movieId>')
def movieDetail(movieId):
    # movieTitle = ""
    # moviePoster = ""
    # movieDes = ""
    # movieCountry = ""
    # movieRuntime = ""
    for movie in movieListDefault:
        if movie.movieId == movieId:
            movieTitle = movie.title
            moviePoster = movie.poster
            movieDes = movie.description
            movieCountry = movie.country
            movieRuntime = movie.runtime
            movieLang = movie.language
            movieRDate = movie.reDate
            movieGenre = movie.genre
            
        # else:
        #     return None
    return render_template('movieDetail.html',movieId=movieId, movieTitle=movieTitle,moviePoster=moviePoster,movieDes=movieDes,
                           movieLang=movieLang,movieRDate=movieRDate,movieCountry=movieCountry,movieRuntime=movieRuntime,movieGenre=movieGenre)
