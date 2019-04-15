import os
import unittest
# from .models import Source, Article
from app.models import Source, Article
# Source  = models.Source
# Article = models.Article

# sys.path.append('./app')


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_source = Source('bbc','BBC', 'Another Crazy News','http://www.bbc.co.uk', 'general','en','gb')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
        


class ArticleTest(unittest.TestCase):
    '''
    Test case to test behavior of the Article class
    ''' 
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_article = Article(
                                'bbc-news',
                                'BBC',
                                'Oduori Gabriel',
                                'Crazy Article', 
                                'Police say four men were shot outside a venue in Melbourne from a car.', 
                                'https://www.engadget.com/2019/03/21/square-will-offer-its-new-crypto-employees-payment-in-bitcoin/',
                                'https://i.kinja-img.com/gawker-media/image/upload/s--FSk-nXyV--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/wihsmbwlreqfqviq7fdc.jpg',
                                '2019-04-14T03:24:12Z',
                                'Image copyright Reuters Image caption Police said the men sustained \"horrific injuries\" outside the venue on Sunday morning One man has been killed and three others wounded in a shooting outside a popular nightclub in the Australian city of Melbourne',
                                )
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
        
if __name__ == "__main__":
    unittest.main()

