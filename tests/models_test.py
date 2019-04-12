import unittest
from app.models import Sources,Articles


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        
        self.new_source = Source()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))

