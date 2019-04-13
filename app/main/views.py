from flask import render_template
from . import main
from ..requests import get_sources#,get_articles

@main.route('/')
def index():
    '''
	View Function that returns the index page and its data
	'''
    business_sources = get_sources('business')
    entertainemnt_sources = get_sources('entertainment')
    science_sources = get_sources('science')
    # print(business_sources)
    headline = 'Home of news Highlights'
    return render_template('index.html', headline=headline, business=business_sources, entertainment = entertainemnt_sources, science = science_sources)