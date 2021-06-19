import unittest
from app.models import Quote


class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quoteclass
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote(1, 'Debbie' , 'its never that serious')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


