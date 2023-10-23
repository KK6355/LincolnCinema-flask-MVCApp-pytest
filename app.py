from flask import Flask,render_template, request
from MovieListDefault import movieListDefault
app = Flask(__name__)
@app.route('/')
def index():
    
    return render_template('index.html',movieListDefault = movieListDefault)
