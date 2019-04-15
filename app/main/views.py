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
    sports_sources = get_sources('sports')
    general_sources = get_sources('general')
    technology_sources = get_sources('technology')
    
    headline = 'Home of news highlights'
    return render_template('index.html', 
                           headline=headline, 
                           business=business_sources, 
                           entertainment = entertainemnt_sources, 
                           science = science_sources,
                           sports = sports_sources,
                           technology = technology_sources,
                           general = general_sources
                           )


@main.route('/highlights')
def top_news():
    '''
    '''
    us_news = get_articles('us')
    uk_news = get_articles('gb')

    
    return render_template('articles.html',us=us_news, gb=uk_news )



@main.route('/articles/<id>')
def articles(id):
    '''
    this function takes in a list of scources anf filters them out by a specific
    source using the source id. For example, if the source is BBC, it will take
    in the "id" as bbc-news
    '''
    aricle = get_article(id)
    
    return render_template('articles.html', id = source)