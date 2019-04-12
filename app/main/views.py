from flask import render_template
from . import main
# from ..request import get_sources,get_articles

@main.route('/')
def index():
	'''
	View Function that returns the index page and its data
	'''

	title = 'NEWS API now starting'

	return render_template('index.html', title=title)