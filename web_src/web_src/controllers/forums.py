import logging

import web_src.lib.helpers as h
import web_src.model as model
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from web_src.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ForumsController(BaseController):

    def index(self):
        category_q = model.Session.query(model.Category)
        c.categories = category_q.all()    	

        return render("forums/index.html")

    def view(self, id):
        c.pageID = id
        return render("forums/page.html")

    def viewforum(self, id):
        return id