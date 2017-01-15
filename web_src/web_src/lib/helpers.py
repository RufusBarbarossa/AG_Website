"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import web_src.model as model

from formbuild.helpers import field
from formbuild import start_with_layout as form_start, end_with_layout as form_end
from webhelpers.html.tags import *

#Temporary Placeholder for a real function - TBD once we get user auth
def getUser():
    return "RufusBarbarossa"

login = False

def getLoggedIn():
    return login

def lastModified(forumID):
	page_q = model.Session.query(model.Page).filter_by(forumid=forumID)
	if len(page_q.all()) == 0:
		return "No Threads"
	else:
		page_q = page_q.order_by(model.page_table.c.lastModified.asc())
		return page_q.first().lastModified

def numThreads(forumID):
	return len(model.Session.query(model.Page).filter_by(forumid=forumID).all())
