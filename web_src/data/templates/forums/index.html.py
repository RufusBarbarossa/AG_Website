# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484238619.408261
_enable_loop = True
_template_filename = '/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/index.html'
_template_uri = 'forums/index.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['scripts', 'title']


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
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n<div class="w3-content" style="max-width:2000px;margin-top:46px">\n\n<h1 style="text-align: center">Forums</h1>\n\n')
        for category in c.categories:
            __M_writer(u'<h2 style="text-align: center; white-space: nowrap;">\n')
            __M_writer(escape(category.title))
            __M_writer(u'\n<a href="javascript:void(0)" onclick="hideshow(\'')
            __M_writer(escape(category.id))
            __M_writer(u'\')" id="')
            __M_writer(escape(category.id))
            __M_writer(u'+" style="text-decoration: none;">+</a>\n<a href="javascript:void(0)" onclick="hideshow(\'')
            __M_writer(escape(category.id))
            __M_writer(u'\')" id="')
            __M_writer(escape(category.id))
            __M_writer(u'-" style="display: none; text-decoration: none;">-</a>\n</h2>\n\n<table class="forums" id="')
            __M_writer(escape(category.id))
            __M_writer(u'" style="display: none">\n\t<tr class="forums">\n\t\t<th class="forums" style="width:10%"> Forum Name </th>\n\t\t<th class="forums" style="width:10%"> Last Modified </th>\n\t\t<th class="forums" style="width:10%"> Num Posts </th>\n\t</tr>\n')
            for forum in category.forums:
                __M_writer(u'\t<tr class="forums" onclick="__goto__(\'')
                __M_writer(escape(h.url(controller='forums', action='viewforum', id=forum.id)))
                __M_writer(u'\')">\n\t\t<td class="forums">')
                __M_writer(escape(forum.title))
                __M_writer(u'</td>\n\t\t<td class="forums">')
                __M_writer(escape(h.lastModified(forum.id)))
                __M_writer(u'</td>\n\t\t<td class="forums">')
                __M_writer(escape(h.numThreads(forum.id)))
                __M_writer(u'</td>\n\t</tr></a>\n')
            __M_writer(u'</table>\n')
        __M_writer(u'\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u' \n<!-- <script> -->\n// Used to toggle the menu on small screens when clicking on the menu button\nfunction hideshow(id) {\n    var x = document.getElementById(id);\n    var plus = document.getElementById(id + "+");\n    var minus = document.getElementById(id + "-");\n\n    if (x.style.display == \'none\') {\n    \tx.style.display = \'block\'\n    \tplus.style.display = \'none\'\n    \tminus.style.display = \'inline-block\'\n\n    }\n    else {\n    \tx.style.display = \'none\'\n    \tplus.style.display = \'inline-block\'\n    \tminus.style.display = \'none\'\n    }\n}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Forums')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"28": 0, "35": 2, "36": 3, "37": 9, "38": 10, "39": 11, "40": 11, "41": 12, "42": 12, "43": 12, "44": 12, "45": 13, "46": 13, "47": 13, "48": 13, "49": 16, "50": 16, "51": 22, "52": 23, "53": 23, "54": 23, "55": 24, "56": 24, "57": 25, "58": 25, "59": 26, "60": 26, "61": 29, "62": 31, "68": 35, "72": 35, "78": 3, "82": 3, "88": 82}, "uri": "forums/index.html", "filename": "/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/index.html"}
__M_END_METADATA
"""
