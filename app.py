from flask import Flask,render_template, request, session,flash,redirect,url_for
from MovieListDefault import movieListDefault
from ScreenListData import screenList
from SeatListData import seatList
from CustomerListData import customerList
from AdminListData import adminList
from StaffListData import staffList
from models.Movie import Movie
from models.Screen import Screen
from HallListData import hallList
app = Flask(__name__)
app.secret_key = "admin123"
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
@app.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    userList = adminList + customerList + staffList
    for user in userList:
        if user.userName == email and user.password == password:
            session["username"] = email
            session["role"] = user.role
            session["userId"] = user.userId
            
        else:
            flash("Invalid user name or password!")

    return redirect(url_for("index")) 
# public interface logout function
@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("role", None)
    session.pop("userId", None)
    return redirect(url_for("index"))
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
@app.route("/manageMovies")
def manageMovies():
    if session["role"]=="admin":
        return render_template("manageMovies.html", movieListDefault = movieListDefault ,screenList=screenList,hallList=hallList)
    else:
        return redirect(url_for("index"))

@app.route("/addMovie", methods=["POST"])
def addMovie():
    title = request.form.get("title")
    language = request.form.get("language")
    genre = request.form.get("genre")
    reDate = request.form.get("reDate")
    newMovie = Movie(title,language,genre,reDate)
    movieListDefault.append(newMovie)
    return redirect(url_for("manageMovies"))
@app.route("/addScreen", methods=["POST"])
def addScreen():
    movieIdStr = request.form.get("movieId")
    movieId = int(movieIdStr)
    hallId = request.form.get("hallId")
    scheduledDate = request.form.get("scheduledDate")
    scheduledTime = request.form.get("scheduledTime")
    newScreen = Screen( movieId, hallId, scheduledDate, scheduledTime)
    screenList.append(newScreen)
    print(len(screenList))
    return redirect(url_for("manageMovies"))

@app.route("/bookTicket", methods=["POST"])
def bookTicket():
    seat = request.form.get("seat")
    print(seat)
    return redirect(url_for("index"))