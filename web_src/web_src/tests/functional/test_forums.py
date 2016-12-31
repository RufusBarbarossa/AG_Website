from web_src.tests import *

class TestForumsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='forums', action='index'))
        # Test response...
