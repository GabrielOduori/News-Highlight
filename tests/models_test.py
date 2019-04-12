# import os
import unittest
from models import Source, Article

# sys.path.append('./app')


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_source = Source('BBC', 'Another Crazy News', 'Gabriel Oduori', '10.12.2019','This is one greate news we need to look at','https://i.kinja-img.com/gawker-media/image/upload/s--FSk-nXyV--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/wihsmbwlreqfqviq7fdc.jpg','https://techcrunch.com/2019/04/11/rasa-raises-13m-led-by-accel-for-its-developer-friendly-open-source-approach-to-chatbots/')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))
        


class ArticleTest(unittest.TestCase):
    '''
    Test case to test behavior of teh Article class
    ''' 
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_article = Article('BBC', 'Crazy Article', 'Oduori Gabriel', '13.04.2019','https://i.kinja-img.com/gawker-media/image/upload/s--FSk-nXyV--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/wihsmbwlreqfqviq7fdc.jpg','content')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
        
if __name__ == "__main__":
    unittest.main()

