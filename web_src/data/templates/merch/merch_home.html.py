# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1483165405.70674
_enable_loop = True
_template_filename = '/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/merch/merch_home.html'
_template_uri = 'merch/merch_home.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="w3-content" style="max-width:2000px;margin-top:46px">\n\n<h1 style="text-align: center">Welcome to Ragna\'s Site - Merch</h1>\n<p style="text-align: center"> Absolutely nothing is implemented, but it exists :p</p>\n\n<p style="text-align: center"> This is the location for the merch page</p>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Merch')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 2, "34": 3, "40": 3, "44": 3, "50": 44, "28": 0}, "uri": "merch/merch_home.html", "filename": "/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/merch/merch_home.html"}
__M_END_METADATA
"""
