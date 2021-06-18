from app.models.quote_test import Quote
from app import app
import urllib.request,json
from .models import quote

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
            quotes_results_list = get_quotes_response['results']
            quotes_results = process_results(quotes_results_list)


    return quotes_results
def process_results(quote_list):
    '''
    Function  that processes the quote result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of movie objects
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote')
        
        quote_object = quote(id,author,quote)
        quote_results.append(quote_object)

    return quote_results
    