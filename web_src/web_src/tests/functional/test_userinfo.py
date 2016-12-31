from web_src.tests import *

class TestUserinfoController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='userinfo', action='index'))
        # Test response...
