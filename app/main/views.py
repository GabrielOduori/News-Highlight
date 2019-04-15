from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Source, Article

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


@main.route('/articles/<id>')
def articles(id):
    '''
    this function takes in a list of scources anf filters them out by a specific
    source using the source id. For example, if the source is BBC, it will take
    in the "id" as bbc-news
    '''
    source = get_articles(id)
    # print(source)
    
    return render_template('articles.html', id=id, source = source)