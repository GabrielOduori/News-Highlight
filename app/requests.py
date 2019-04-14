import urllib.request, json
from .models import Source, Article
# from app import app

# Getting the AP Key
api_key = '0e2d34b1f7d5483999ae74a1dead1039'
# api_key = None

# Getting the News base URL
base_url = 'https://newsapi.org/v2/sources?language=en&category={}&apikey={}'
articles_base_url='https://newsapi.org/v2/top-headlines?country={}&apiKey={}'
# base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_BASE_URL']
    
    


def get_sources(category):
    '''
    Function that gets the 
    '''
    # print(base_url)
    get_sources_url = base_url.format(category,api_key)
    # print(api_key)
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

            
        # source_object = Source(name,title,author,published_at,description,urlToImage,url)
        # source_object = Source(id,name,description,url)

        # sources_list.append(source_object)
    # print(processed_results)
    return processed_results



def get_articles(country):
    '''
    '''
    pass

    get_article_url  = articles_base_url.format(country,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)
        
        article_result = []
        
        if article_response['articles']:
            article_list = article_response['articles']
            article_result = process_article_results(article_list)
            
    return article_result


def process_article_results(article_result):
    
    processed_articles = []
    
    for article_item in article_result:
        # id = sources_list.get('id')
        name = article_item.get('name')
        author  = article_item.get('author')
        title  = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content') 
        
        if url:
            article_object = Article(name,author,title,description,url,urlToImage,publishedAt,content)
            processed_articles.append(article_object)
            
    # print(processed_articles)
    return processed_articles
        
        
        

# def search_articles(source):
#     '''
#     '''
    
#     search_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(api_key,source)
#     with urllib.request.urlopen(search_url) as url:
#         pass
        