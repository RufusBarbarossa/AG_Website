import logging

import web_src.lib.helpers as h
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from web_src.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ForumsController(BaseController):

    def index(self):
        return render("forums/index.html")