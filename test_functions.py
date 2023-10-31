from app import app
import flask
import os
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
        response = test_client.post('/addMovie')
        if response.status_code == 200:
            assert b'Manage Movies & Screens' in response.data


                