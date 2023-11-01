from app import app
import flask
import os
from models.Customer import Customer
from CustomerListData import customerList
from MovieListDefault import movieListDefault
from ScreenListData import screenList
os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
def test_index():  
    with app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Now Showing" in response.data
def test_myTickets():
    with app.test_client() as test_client:
        response = test_client.get('/myTickets')
        if "role" in flask.session and flask.session['role']=='customer':
            assert response.status_code == 200
            assert b"My Tickets" in response.data

def test_tickets():
    with app.test_client() as test_client:
        response = test_client.get('/tickets')
        if "role" in flask.session and flask.session['role']=='staff':
            assert response.status_code == 200
            assert b"Tickets" in response.data
def test_register():
    with app.test_client() as test_client:
        response = test_client.post('/register',data={"userName":"test@test.com","password":"123456"})
        if response.status_code == 200:
            assert len(customerList) == 3
            assert customerList[len(customerList)-1].userName == "test@test.com"
def test_login():
    with app.test_client() as test_client:
        response = test_client.post('/login')
        if response.status_code == 200:
            assert b'hi' in response.data
            assert "role" in flask.session
def test_logout():
    with app.test_client() as test_client:
        response = test_client.post('/logout')
        if response.status_code == 200:
            assert b"hi" not in response.data
            assert "role" not in flask.session
def test_searchMovie():
    with app.test_request_context('/?searchStr=moon'):
        assert flask.request.path == '/'
        assert flask.request.args['searchStr'] == 'moon'
def test_movieDatail():
     with app.test_client() as test_client:
        response = test_client.get('/movieDetail/4000')       
        assert response.status_code == 200
        assert b"Killers of the Flower Moon" in response.data
def test_manageMovies():
    with app.test_client() as test_client:
        response = test_client.get('/manageMovies')
        if "role" in flask.session and flask.session['role']=='admin':
            assert response.status_code == 200
            assert b"Manage Movies & Screens" in response.data
def test_addMovie():
    with app.test_client() as test_client:
        response = test_client.post('/addMovie',data={"title":"Harry Potter","language":"English","genre":"Adventure","reDate":"2000-1-1"})
        if response.status_code == 200:
            assert b'Manage Movies & Screens' in response.data
            assert len(movieListDefault) == 5
            assert movieListDefault[len(movieListDefault)-1].title == "Harry Potter"
def test_addScreen():
    with app.test_client() as test_client:
        response = test_client.post('/addScreen',data={"movieId":4000, "hallId":1, "scheduledDate":"2023-11-30", "scheduledTime":"10:00"})
        if response.status_code == 200:
            assert b'Manage Movies & Screens' in response.data
            assert len(screenList) == 10
            assert screenList[len(screenList)-1].movieId == 4000

                