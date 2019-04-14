from flask import render_template
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():
    '''
	View Function that returns the index page and its data
	'''
    business_sources = get_sources('business')
    entertainemnt_sources = get_sources('entertainment')
    science_sources = get_sources('science')
    headline = 'Home of news highlights'
    return render_template('index.html', headline=headline, business=business_sources, entertainment = entertainemnt_sources, science = science_sources)


@main.route('/highlights')
def top_news():
    '''
    '''
    us_news = get_articles('us')
    uk_news = get_articles('gb')

    
    return render_template('articles.html',us=us_news, gb=uk_news )
    