
class Source:
    '''
    Source Class to define new sources object
    Args:
        1. id
        2. name
        3. description:description of the article
        4. url : link to the article on the parent website
        5. category: : article image
        6. language: link to the article on the parent website.
        7. country:
    '''
  
    def __init__(self,id,name,description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        


class Article:
    '''
	Article Class to define Article Objects
	'''
    def __init__ (self,id,source,author,title, description,url,urlToImage, publishedAt,content):
        '''
        Function to initialize Article Objects and defines properties 
        each Article object holds.
        
		Args: 
		1. source
		2. author
		3. title
		4. description
        5. url
		5. urlToImage
		6. content
        7. publishedAt
        8. content
		'''
        self.id = id
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
		