"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from pylons import request, response, session, tmpl_context as c, url

#Temporary Placeholder for a real function - TBD once we get user auth
def getUser():
    return "RufusBarbarossa"

login = False

def getLoggedIn():
    return login

