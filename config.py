import os

class Config:
    # NEWS_SOURCE_URL='https://newsapi.org/v2/sources?apiKey='
    NEWS_SOURCE_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apikey={}'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    
    
class ProdConfig(Config):
    pass
    

class DevConfig(Config):
    DEBUG = True
        
        
        
config_options = { 
    'development' : DevConfig,
    'production' : ProdConfig
}