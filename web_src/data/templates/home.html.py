# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1483243595.845813
_enable_loop = True
_template_filename = '/home/pi/Documents/My Projects/MainAG/web_src/web_src/templates/home.html'
_template_uri = 'home.html'
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
        __M_writer(u'\n\n<div class="w3-content" style="max-width:2000px;margin-top:46px">\n<h1 style="text-align: center">Welcome to Ragna\'s Site - Home Page</h1>\n<p style="text-align: center"> Absolutely nothing is implemented, but it exists :p</p>\n\n<p style="text-align: center"> This is the location for the home page</p>\n\n<iframe src="https://discordapp.com/widget?id=189563877086855168&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0"></iframe>\n\n\n<iframe style="width: 620px; height: 378px;" scrolling="no" frameborder="0" src="https://www.twitch.tv/abandon_gaming/embed"></iframe>\n\n<iframe style="width: 350px; height: 379px;" scrolling="no" frameborder="0" src="https://www.twitch.tv/abandon_gaming/chat?popout="></iframe>\n\n<center>\n\t    <a href="https://www.twitch.tv/abandon_gaming?tt_medium=live_embed&tt_content=text_link" style="padding: 2px 0px 4px; width: 345px; font-size: 10px; font-weight: normal; text-decoration: underline; display: block;">Watch live video from Abandon Gaming on www.twitch.tv</a>\n\n</center>\n\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 2, "34": 3, "40": 3, "44": 3, "50": 44, "28": 0}, "uri": "home.html", "filename": "/home/pi/Documents/My Projects/MainAG/web_src/web_src/templates/home.html"}
__M_END_METADATA
"""
