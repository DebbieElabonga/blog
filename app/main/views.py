from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quotes

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting quotes
    quotes = get_quotes()
    return render_template('index.html',quotes=quotes)