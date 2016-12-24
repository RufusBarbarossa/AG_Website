import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from web_src.lib.base import BaseController, render

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def index(self):
        if request.params.has_key('name'):
            c.name = request.params['name']
        return render('/index.html')

    def debug(self):
        result = '<html><body><h1>Environ</h1>'
        for key, value in request.environ.items():
            result += '<b>%s</b>: %r <br />'%(key, value)

        result += '<h1>Headers</h1>'
        for key, value in request.headers.items():
            result += '<b>%s</b>: %r <br />'%(key, value)

        result += '<h1>Method</h1>%s<br />'%request.method

        result += '<h1>Params</h1>'
        if len(request.params) == 0:
            result += 'No Parameters'
        for key, value in request.params.items():
            result += '<b>%s</b>: %r <br />'%(key, value)

        result += '<h1>Cookies</h1>'
        if len(request.cookies) == 0:
            result += 'No Cookies'
        for key, value in request.cookies.items():
            result += '<b>%s</b>: %r <br />'%(key, value)

        result += "</body></html>"
        return result

    def testException(self):
        num = 34
        raise Exception('Testing exception number %d'%(num))