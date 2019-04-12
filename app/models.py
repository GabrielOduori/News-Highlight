
class Source:
    '''
    Source Class to define new sources object
    Args:
        1. name
        2. title
        3. author
        4. published_at : Date of publication
        5. description : description of the article
        6. urlToImage : article image
        7. url : link to the article on the parent website.
    '''
    def __init__(self,name, title, author,published_at, description, urlToImage, url):
        self.name = name
        self.title  = title
        self.author  = author
        self.published_at = published_at
        self.description = description
        self.urlToImage = urlToImage
        self.url = url


class Article:
	'''
	Article Class to define Article Objects
	'''
	def __init__(self,name, title, author, published_at,urlToImage, content):
		'''
		Function to initialize Article Objects and defines properties 
        each Article object holds.
	
		Args: 
			1. name
			2. title
			3. author
			4. published_at
			5. urlToImage
			6. content
		'''
		self.name = name
  		self.title = title
        self.author = author
        self.published_at = published_at
        self.urlToImage = urlToImage
        self.content = content
		