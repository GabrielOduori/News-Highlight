import urllib.request, json
from .models import Source, Article
from .base import *

# Getting the AP Key
api_key = None

# Getting the News base URL
base_url  = None

def configure_request(app):
    print('configure_request')
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']
    
    


def get_sources(category):
    '''
    Function that gets the 
    '''
    if base_url is None:
        configure_request(app)
    print(base_url)
    print(category)
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url ) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        # sources_results = None
        sources_results = []
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)
            
    return sources_results



def process_sources(sources_results):
    '''
    '''
    
    sources_list = []
    
    for source in sources_results:
        id = source.get('id')
        name = source.get('name')
        # title  = source.get('title')
        # author  = source.get('author')
        # published_at = source.get('published_at')
        description = source.get('description') 
        # urlToImage = source.get('urlToImage')
        url = source.get('url')
        
        # source_object = Source(name,title,author,published_at,description,urlToImage,url)
        source_object = Source(id,name,description,url)

        sources_list.append(source_object)
        
    return sources_list