import urllib.request, json
from .models import Source, Article
# from app import app

# Getting the AP Key
api_key = '0e2d34b1f7d5483999ae74a1dead1039'
# api_key = None

# Getting the News base URL
base_url = 'https://newsapi.org/v2/sources?language=en&category={}&apikey={}'
# base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']
    
    


def get_sources(category):
    '''
    Function that gets the 
    '''
    # print(base_url)
    get_sources_url = base_url.format(category,api_key)
    print(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        # sources_results = None
        sources_results = []
        
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
            
    return sources_results



def process_results(sources_results):
    '''
    '''
    
    processed_results = []
    
    
    for sources_list in sources_results:
        id = sources_list.get('id')
        name = sources_list.get('name')
        # title  = source.get('title')
        # author  = source.get('author')
        # published_at = source.get('published_at')
        description = sources_list.get('description') 
        # urlToImage = source.get('urlToImage')
        url = sources_list.get('url')
        
        if url:
            sources_object = Source(id, name,description,url)
            processed_results.append(sources_object)

            
        # source_object = Source(name,title,author,published_at,description,urlToImage,url)
        # source_object = Source(id,name,description,url)

        # sources_list.append(source_object)
    print(processed_results)
    return processed_results