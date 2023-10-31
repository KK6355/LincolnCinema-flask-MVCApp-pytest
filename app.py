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
from models.Booking import Booking
from models.Customer import Customer
from CouponListData import couponList
from models.CreditCard import CreditCard
from models.DebitCard import DebitCard
from models.Notification import Notification
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
            print("Invalid user name or password!")
    
    return redirect(url_for("index")) 
@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    emailList = []
    for customer in customerList:
        emailList.append(customer.userName)
    if email not in emailList:
        newCus = Customer(email, password)
        customerList.append(newCus)
        print(newCus.userName)
        print(len(customerList))       
    else:
        flash("Email exists!Please use another one!") 
        print("Email exists!Please use another one!")

    return redirect(url_for("index")) 
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
                           screens=screens,seatList = seats,customerList=customerList )
@app.route("/manageMovies")
def manageMovies():
    if "role" in session and session["role"]=="admin":
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
    hallIdStr = request.form.get("hallId")
    hallId = int(hallIdStr)
    scheduledDate = request.form.get("scheduledDate")
    scheduledTime = request.form.get("scheduledTime")
    newScreen = Screen( movieId, hallId, scheduledDate, scheduledTime)
    screenList.append(newScreen)
    print(len(screenList))
    return redirect(url_for("manageMovies"))

@app.route("/bookTicket", methods=["POST"])
def bookTicket():
    if session["role"] == "staff":
        customerIdStr = request.form.get("customerId")
        customerId = int(customerIdStr)
    if session["role"] == "customer":
        customerId = session["userId"]
    bookingList = []
    for customer in customerList:
        if customer.userId == int(customerId):
            bookingList = customer.bookingList
       
    screenIdList = []
    
    for seat in seatList:
        for screen in screenList:
            if request.form.get(f"seat{seat.seatId}{screen.screenId}"):                
                screenIdList.append(screen.screenId)
               

    # add into customer booking list  
    screenIdListUnique = list(set(screenIdList))
    for screenId in  screenIdListUnique:
        newBooking = Booking(int(screenId),customerId)
        bookingList.append(newBooking)
        for seat in seatList:
            if request.form.get(f"seat{seat.seatId}{screenId}"):
                newBooking.seatList.append(seat.seatId)
                #print(newBooking.seatList)
    #change seats status
                for screen in screenList:
                     if screen.screenId == screenId:
                       
                        screen.unavailableSeats.append(seat.seatId)    
    if session["role"] == "staff":
        return redirect(url_for("tickets"))
    if session["role"] == "customer":
        return redirect(url_for("myTickets")) 
    
   
@app.route("/myTickets")
def myTickets():
    if "role" in session and session["role"]=="customer":
        bookingList = []
        coupons = []
       
        for coupon in couponList:
            if coupon.customerId == session["userId"]:
                coupons.append(coupon)
        for customer in customerList:
            if customer.userId == session["userId"]:
                bookingList = customer.bookingList
                for booking in bookingList:
                    booking.payment = 0
                    for seatId in booking.seatList:
                        for seat in seatList:
                            if seat.seatId == seatId:
                                booking.payment += seat.price
        return render_template("myTickets.html", bookingList=bookingList,screenList=screenList,movieList=movieListDefault, seatList=seatList,hallList=hallList,coupons=coupons)
    else:
        return redirect(url_for("index"))
@app.route("/tickets")
def tickets():
    if "role" in session and session["role"]=="staff":
        bookingList =  []
        for customer in customerList:
            for booking in customer.bookingList:
                bookingList.append(booking)
                booking.payment = 0
                for seatId in booking.seatList:
                    for seat in seatList:
                        if seat.seatId == seatId:
                            booking.payment += seat.price
        print(bookingList)
    
        return render_template("myTickets.html", bookingList=bookingList,screenList=screenList,movieList=movieListDefault, seatList=seatList,hallList=hallList,customerList=customerList,couponList=couponList)
    else:
        return redirect(url_for("index")) 

@app.route("/payTicket",methods=['POST'])
def payTicket():
    
    if session["role"] == "staff":
        customerIdStr = request.form.get("customerId")
        customerId = int(customerIdStr)
    if session["role"] == "customer":
        customerId = session["userId"]
    paymethod = request.form.get("paymethod")
    paymentStr = request.form.get("payment")
    payment = float(paymentStr)
    couponId = request.form.get("couponId")
    
    #change booking status and payment
    
    bookingIdStr = request.form.get("bookingId")
    bookingRefNum = int(bookingIdStr)
    for customer in customerList:
            if customer.userId == customerId:
                if couponId:
                    for coupon in couponList:
                        if coupon.couponId == int(couponId):
                            coupon.status = "used"
                            payment = payment * (1-coupon.discount)
                if paymethod == "creditCard":
                    cardNum = request.form.get("cardNum")
                    holderName = request.form.get("holderName")
                    type = request.form.get("type")
                    expiration = request.form.get("expiration")
                    newCreditCard = CreditCard(cardNum, holderName,type,expiration)
                    customer.cardList.append(newCreditCard)
                    newCreditCard.balance = newCreditCard.balance - payment
                    
                if paymethod == "debitCard":
                    cardNum = request.form.get("cardNum")
                    holderName = request.form.get("holderName")
                    type = request.form.get("type")
                    newDebitCard = DebitCard(cardNum, holderName,type)
                    customer.cardList.append(newDebitCard)
                    newDebitCard.balance = newDebitCard.balance - payment
                    
                newNotification = Notification("payTicket",f"You have paid ${payment}.Your tickets have been booked successfully! ")
                customer.notificationList.append(newNotification)
               
                print(newNotification.content)
                bookingList = customer.bookingList
                for booking in bookingList:
                    if booking.refNum ==  bookingRefNum:
                        booking.payStatus = "paid"
                        booking.payment = payment
                        booking.paymethod = paymethod
    # #change seats status
    #                     for screen in screenList:
    #                         if screen.screenId == booking.screenId:
    #                             for seatId in booking.seatList:
    #                                 screen.unavailableSeats.append(seatId)

    
    
    if session["role"] == "staff":
        return redirect(url_for("tickets"))
    if session["role"] == "customer":
        return redirect(url_for("myTickets")) 
@app.route("/cancelTicket",methods=['POST'])
def cancelTicket():
    if session["role"] == "staff":
        customerIdStr = request.form.get("customerId")
        customerId = int(customerIdStr)
    if session["role"] == "customer":
        customerId = session["userId"]
    bookingIdStr = request.form.get("bookingId")
    bookingRefNum = int(bookingIdStr)
    for customer in customerList:
            if customer.userId == customerId:
                bookingList = customer.bookingList
                for booking in bookingList:
                    if booking.refNum ==  bookingRefNum:
                        if booking.payStatus == 'unpaid':
                            customer.bookingList.remove(booking)
                            # release seats
                            for screen in screenList:
                                if screen.screenId == booking.screenId:
                                    for seatId in booking.seatList:
                                        screen.unavailableSeats.remove(seatId)
                        else:
                            # refund
                            if booking.paymethod != "cash":
                                defaultCard = customer.cardList[0]
                                defaultCard.balance = defaultCard.balance + booking.payment
                            # release seats
                            for screen in screenList:
                                if screen.screenId == booking.screenId:
                                    for seatId in booking.seatList:
                                        screen.unavailableSeats.remove(seatId)
                            # remove from list
                            customer.bookingList.remove(booking)
                            #create new notification
                            newNotification = Notification("cancelTicket",f"${booking.payment} refund.Your tickets have been cancelled successfully! ")
                            customer.notificationList.append(newNotification)
                            print(newNotification.content)
    if session["role"] == "staff":
        return redirect(url_for("tickets"))
    if session["role"] == "customer":
        return redirect(url_for("myTickets")) 

@app.route("/cancelScreen",methods=['POST'])
def cancelScreen():
    screenIdStr = request.form.get("screenId")
    screenId = int(screenIdStr)
    bookingList =  []
    for customer in customerList:
        for booking in customer.bookingList:
            bookingList.append(booking)
    
    for booking in bookingList:
        if booking.screenId == screenId:
            booking.payStatus = "unpaid"
            
            for customer in customerList:
                if booking.customerId == customer.userId:
                    if booking.paymethod != "cash":
                        card = customer.cardList[0]
                        card.balance += booking.payment
                        booking.payment = 0
                    customer.bookingList.remove(booking)
            
    
    for screen in screenList:
        if screen.screenId == screenId:
            screen.unavailableSeats = []
            screenList.remove(screen)

    return redirect(url_for("manageMovies"))
@app.route("/cancelMovie",methods=['POST'])
def cancelMovie():
    movieIdStr = request.form.get("movieId")
    movieId = int(movieIdStr)
    bookingList =  []
    for customer in customerList:
        for booking in customer.bookingList:
            bookingList.append(booking)
    for screen in screenList:
        if screen.movieId == movieId:
            for booking in bookingList:
                if booking.screenId == screen.screenId:
                    booking.payStatus = "unpaid"
            
                    for customer in customerList:
                        if booking.customerId == customer.userId:
                            if booking.paymethod != "cash":
                                card = customer.cardList[0]
                                card.balance += booking.payment
                                booking.payment = 0
                            customer.bookingList.remove(booking)
            screen.unavailableSeats = []
            screenList.remove(screen) 
    for movie in movieListDefault:
        if movie.movieId == movieId:
            movieListDefault.remove(movie) 

    return redirect(url_for("manageMovies"))