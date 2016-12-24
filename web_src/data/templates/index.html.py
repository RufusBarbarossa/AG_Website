# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1482201528.589585
_enable_loop = True
_template_filename = '/home/adstanes/Documents/Web/AG_Website/web_src/web_src/templates/index.html'
_template_uri = '/index.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        str = context.get('str', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<html>\n<head>\n    <title>Greetings</title>\n</head>\n<body>\n    <h1>Greetings</h1>\n    <p>\n')
        if hasattr(c, 'name'):
            __M_writer(u'    Hello ')
            __M_writer(escape(c.name))
            __M_writer(u'!\n')
        else:
            __M_writer(u'    Welcome Guest\n')
        __M_writer(u'    </p>\n\n<p>\n')
        for key in context.keys():
            __M_writer(u'The key is <tt>')
            __M_writer(escape(key))
            __M_writer(u'</tt>, the value is ')
            __M_writer(escape(str(context.get(key))))
            __M_writer(u'. <br />\n')
        __M_writer(u'</p>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 13, "33": 16, "34": 17, "35": 17, "36": 17, "37": 17, "38": 17, "39": 19, "45": 39, "17": 0, "25": 1, "26": 8, "27": 9, "28": 9, "29": 9, "30": 10, "31": 11}, "uri": "/index.html", "filename": "/home/adstanes/Documents/Web/AG_Website/web_src/web_src/templates/index.html"}
__M_END_METADATA
"""
