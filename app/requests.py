import urllib.request, json
from .models import Source, Article

# Getting the AP Key
api_key = None

# Getting the News base URL
base_url  = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCE_URL']