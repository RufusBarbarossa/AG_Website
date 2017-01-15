# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484262801.320168
_enable_loop = True
_template_filename = '/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/new.html'
_template_uri = '/forums/new.html'
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
        __M_writer(u'\n\n<div class="w3-content" style="max-width:2000px;margin-top:46px">\n\n<h1 style="text-align: center">New Thread</h1>\n\n')
        __M_writer(escape(h.form_start(h.url(controller='forums', action='create'), method="post", class_='newpage', id='newpage')))
        __M_writer(u'\n\t')
        __M_writer(escape(h.field(
    	"Title",
    	h.text(name='title'),
    	required=True,
	)))
        __M_writer(u'\n\t')
        __M_writer(escape(h.field(
    	"Forum ID ",
    	h.text(name='forumid', value=c.forumid),
    	required=True,
    	field_desc = "The forum that this thread will be a part of"
	)))
        __M_writer(u'\n\t')
        __M_writer(escape(h.field(
    	"Content ",
    	h.textarea(name='content', rows=7, class_="newpage"),
    	required=True,
    	field_desc = 'The text that will make up the body of the page'
	)))
        __M_writer(u'\n    ')
        __M_writer(escape(h.field(field=h.submit(value="Create Page", name='submit'))))
        __M_writer(u'\n')
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u" \n<!-- <script> -->\n\nfunction findWidth() {\n\tvar position = document.getElementById('newpage').getBoundingClientRect();\n\tconsole.log(position.width);\n}\n\n")
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
{"source_encoding": "utf-8", "line_map": {"35": 2, "36": 3, "37": 9, "38": 9, "39": 10, "72": 32, "60": 27, "44": 14, "45": 15, "78": 3, "82": 3, "51": 20, "52": 21, "88": 82, "68": 32, "58": 26, "59": 27, "28": 0, "61": 28, "62": 28}, "uri": "/forums/new.html", "filename": "/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/new.html"}
__M_END_METADATA
"""
