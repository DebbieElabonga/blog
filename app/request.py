
import urllib.request,json
from .models import quote
from app import app

Quote = quote.Quote

# Getting the movie base url
base_url = app.config["QUOTES_API_BASE_URL"]

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:
            quotes_results_list = get_quotes_response
            
    return quotes_results_list
