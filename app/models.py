class Sources:
    '''
    Class to define sources object
    '''
    def __init__(self, name, author, title, description, url, urlToImage, published_at, content):
        self.name = name
        self.author  = author
        self.title  = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.published_at = published_at
        self.content = content



class Articles:
    '''
    Class to define Article object
    '''
    
    def __init__(self, id, name):
        self.id = id
        self.name = name



