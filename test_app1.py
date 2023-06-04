from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/projects/') # different
def projects():
    return 'The project page'

@app.route('/about') # unique
def about():
    return 'The about page'

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context(): # can start to build up a complex url system
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))