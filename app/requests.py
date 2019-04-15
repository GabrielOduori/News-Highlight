import urllib.request, json
from .models import Source, Article
# from app import app

# Getting the AP Key
api_key = '0e2d34b1f7d5483999ae74a1dead1039'
# api_key = None

# Getting the News base URL
base_url = 'https://newsapi.org/v2/sources?language=en&category={}&apikey={}'
articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_BASE_URL']
    
    


def get_sources(category):
    '''
    Function that gets the 
    '''
    get_sources_url = base_url.format(category,api_key)

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
        description = sources_list.get('description') 
        url = sources_list.get('url')
        category = sources_list.get('category')
        language  =  sources_list.get('language')
        country = sources_list.get('country')
        if url:
            sources_object = Source(id, name,description,url,category,language,country)
            processed_results.append(sources_object)

    
    return processed_results


def get_articles(id):
    
    get_article_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_articles_response = json.loads(get_article_data)
        
        article_results = None
        
        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)
            
    return article_results
    
    
    
    
    
def process_articles(article_results):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain the articles details
    Returns :
        articles_results: A list of articles objects
    '''
    articles_results= []
    
    for article_item in article_results:
        id = article_item.get('id')
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        # if id:
        articles_object = Article(id,source,author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(articles_object)    
    return articles_results
        
        
        
