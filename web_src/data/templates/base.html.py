# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484464078.568016
_enable_loop = True
_template_filename = u'/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/base.html'
_template_uri = u'/base.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <link rel="stylesheet" href="/css/baseStyle.css">\n  <link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">\n  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">\n  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n  <style>\n    body {font-family: "Lato", sans-serif}\n    .mySlides {display: none}\n  </style>\n  <title>')
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n</head>\n\n<body>\n<!-- Navbar -->\n<div class="w3-top">\n<ul class="w3-navbar w3-black w3-card-2 w3-left-align">\n  <li class="w3-hide-large w3-opennav w3-right">\n    <a class="w3-padding-large" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>\n  </li>\n  <li><a href="')
        __M_writer(escape(h.url(controller='index', action='home')))
        __M_writer(u'" class="w3-hover-none w3-hover-text-grey w3-padding-large">HOME</a></li>\n  <li class="w3-hide-small w3-hide-medium"><a href="')
        __M_writer(escape(h.url(controller='forums', action='index')))
        __M_writer(u'" class="w3-padding-large">FORUMS</a></li>\n  <li class="w3-hide-small w3-hide-medium"><a href="')
        __M_writer(escape(h.url(controller='index', action='events')))
        __M_writer(u'" class="w3-padding-large">EVENTS</a></li>\n  <li class="w3-hide-small w3-hide-medium"><a href="')
        __M_writer(escape(h.url(controller='index', action='merch')))
        __M_writer(u'" class="w3-padding-large">MERCH</a></li>\n  <li class="w3-hide-small w3-hide-medium"><a href="')
        __M_writer(escape(h.url(controller='index', action='contact')))
        __M_writer(u'" class="w3-padding-large">CONTACT US</a></li>\n')
        if h.getLoggedIn():
            __M_writer(u'  <li class="w3-hide-small w3-hide-medium w3-dropdown-hover w3-right">\n    <a href="javascript:void(0)" class="w3-hover-none w3-padding-large w3-right" title="User Settings">')
            __M_writer(escape(h.getUser()))
            __M_writer(u' <i class="fa fa-caret-down"></i></a>     \n    <div class="w3-dropdown-content w3-gray w3-card-4">\n      <a href="')
            __M_writer(escape(h.url(controller='userinfo', action='user_settings')))
            __M_writer(u'">Profile Settings</a>\n      <a href="')
            __M_writer(escape(h.url(controller='userinfo', action='notifs')))
            __M_writer(u'">Notifications</a>\n      <a href="')
            __M_writer(escape(h.url(controller='userinfo', action='logout')))
            __M_writer(u'">Log Out</a>\n    </div>\n  </li>\n')
        else:
            __M_writer(u'  <li class="w3-hide-small w3-hide-medium w3-right"><a href="')
            __M_writer(escape(h.url(controller='userinfo', action='login')))
            __M_writer(u'" class="w3-padding-large">LOG IN</a></li>\n  <li class="w3-hide-small w3-hide-medium w3-right"><a href="')
            __M_writer(escape(h.url(controller='userinfo', action='register')))
            __M_writer(u'" class="w3-padding-large">REGISTER</a></li>\n')
        __M_writer(u'</ul>\n</div>\n\n<!-- Navbar on small screens -->\n<div id="tinyNav" class="w3-hide w3-hide-large w3-top" style="margin-top:46px">\n  <ul class="w3-navbar w3-left-align w3-black">\n    <li><a class="w3-padding-large" href="')
        __M_writer(escape(h.url(controller='forums', action='index')))
        __M_writer(u'">FORUMS</a></li>\n    <li><a class="w3-padding-large" href="')
        __M_writer(escape(h.url(controller='index', action='events')))
        __M_writer(u'">EVENTS</a></li>\n    <li><a class="w3-padding-large" href="')
        __M_writer(escape(h.url(controller='index', action='merch')))
        __M_writer(u'">MERCH</a></li>\n    <li><a class="w3-padding-large" href="')
        __M_writer(escape(h.url(controller='index', action='contact')))
        __M_writer(u'">CONTACT US</a></li>\n')
        if h.getLoggedIn():
            __M_writer(u'    <li><a class="w3-padding-large" href="{h.url(controller=\'userinfo\', action=\'user_settings\')}">USER SETTINGS</a></li>\n    <li><a class="w3-padding-large" href="')
            __M_writer(escape(h.url(controller='userinfo', action='notifs')))
            __M_writer(u'">NOTIFICATIONS</a></li>\n    <li><a class="w3-padding-large w3-red w3-hover-pale-red" href="')
            __M_writer(escape(h.url(controller='userinfo', action='logout')))
            __M_writer(u'">LOG OUT</a></li>\n')
        else:
            __M_writer(u'    <li><a class="w3-padding-large w3-green w3-hover-pale-green" href="')
            __M_writer(escape(h.url(controller='userinfo', action='login')))
            __M_writer(u'">REGISTER</a></li>\n    <li><a class="w3-padding-large w3-green w3-hover-pale-green" href="')
            __M_writer(escape(h.url(controller='userinfo', action='register')))
            __M_writer(u'">LOG IN</a></li>\n')
        __M_writer(u'  </ul>\n</div>\n\n')
        __M_writer(escape(self.body()))
        __M_writer(u'\n\n</body>\n\n<script>\n// Used to toggle the menu on small screens when clicking on the menu button\nfunction myFunction() {\n    var x = document.getElementById("tinyNav");\n    if (x.className.indexOf("w3-show") == -1) {\n        x.className += " w3-show";\n    } else { \n        x.className = x.className.replace(" w3-show", "");\n    }\n}\n\nfunction __goto__(url) {\n  console.log(url); \n  window.location = url;\n}\n\n')
        __M_writer(escape(self.scripts()))
        __M_writer(u'\n\n</script>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"17": 0, "24": 1, "25": 13, "26": 13, "27": 23, "28": 23, "29": 24, "30": 24, "31": 25, "32": 25, "33": 26, "34": 26, "35": 27, "36": 27, "37": 28, "38": 29, "39": 30, "40": 30, "41": 32, "42": 32, "43": 33, "44": 33, "45": 34, "46": 34, "47": 37, "48": 38, "49": 38, "50": 38, "51": 39, "52": 39, "53": 41, "54": 47, "55": 47, "56": 48, "57": 48, "58": 49, "59": 49, "60": 50, "61": 50, "62": 51, "63": 52, "64": 53, "65": 53, "66": 54, "67": 54, "68": 55, "69": 56, "70": 56, "71": 56, "72": 57, "73": 57, "74": 59, "75": 62, "76": 62, "77": 82, "78": 82, "84": 78}, "uri": "/base.html", "filename": "/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/base.html"}
__M_END_METADATA
"""
