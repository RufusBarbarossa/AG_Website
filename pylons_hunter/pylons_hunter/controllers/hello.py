import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons import app_globals
from pylons import config
from routes import url_for

from pylons_hunter.lib.base import BaseController, render

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/hello.mako')
        # or, return a string
        return '<b>Hey-o</b>'

    def environ(self):
        result = '<html><body><h1>Environ</h1>'
        for key, value in request.environ.items():
            result += '%s: %r <br />'%(key, value)
        result += '</body></html>'
        return result

    def app_globals_test(self):
        app_globals.visits += 1
        return "You are visitor number %s." % app_globals.visits