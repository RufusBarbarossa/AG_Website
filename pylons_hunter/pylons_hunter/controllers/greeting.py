import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylons_hunter.lib.base import BaseController, render

log = logging.getLogger(__name__)

class GreetingController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/greeting.mako')
        # or, return a string
        c.name = 'Hunter'
        return render ('/greeting.html')
