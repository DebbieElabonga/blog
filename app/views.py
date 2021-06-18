from flask import render_template
from app import app
from .request import get_quotes

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting quotes
    quotes = get_quotes()
    return render_template('index.html',quotes=quotes)