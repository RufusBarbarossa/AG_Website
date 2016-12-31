import logging

import web_src.lib.helpers as h
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from web_src.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UserinfoController(BaseController):

    def login(self):
    	h.login = True
        return render('/user/login.html')

    def register(self):
        return render('/user/register.html')

    def user_settings(self):
    	return render('/user/settings.html')

    def notifs(self):
    	return render('/user/notification.html')

    def logout(self):
    	h.login = False
    	return render('/user/logout.html')