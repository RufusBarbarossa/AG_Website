# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1480716112.689319
_enable_loop = True
_template_filename = '/home/hunter/Documents/AGWebsite/pylons_hunter/pylons_hunter/templates/greeting.html'
_template_uri = '/greeting.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n\t<head>\n\t\t<title>Greetings</title>\n\t</head>\n\t<body>\n\t\t<h1>Greetings</h1>\n\t\t<p>Hello ')
        __M_writer(escape(c.name))
        __M_writer(u'!</p>\n\t</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"24": 7, "17": 0, "31": 25, "25": 7, "23": 1}, "uri": "/greeting.html", "filename": "/home/hunter/Documents/AGWebsite/pylons_hunter/pylons_hunter/templates/greeting.html"}
__M_END_METADATA
"""
