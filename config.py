import os

class Config:
    NEWS_API_URL=''
    SECRET_KEY=''
    
    class ProdConfig(Config):
        pass
    
    
    class DevConfig(Config):
        DEBUG = True
        
        
        config_options = {
            
            'development':DevConfig,
            'production':ProdConfig
        }