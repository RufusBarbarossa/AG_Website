import logging

import web_src.lib.helpers as h
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from web_src.lib.base import BaseController, render

log = logging.getLogger(__name__)

class IndexController(BaseController):

    def home(self):
        c.url = url(controller="index", action="kappa")
        return render('home.html')
   
    def events(self):
        return render('events/events_home.html')

    def merch(self):
        return render('merch/merch_home.html')

    def contact(self):
        return render('contact.html')