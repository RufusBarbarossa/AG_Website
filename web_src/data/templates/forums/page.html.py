# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484467213.703486
_enable_loop = True
_template_filename = '/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/page.html'
_template_uri = 'forums/page.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['insertSpace', 'buildcomment', 'insertSpaceBorder', 'scripts', 'title']


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
        c = context.get('c', UNDEFINED)
        _search_ = context.get('_search_', UNDEFINED)
        h = context.get('h', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _search_first_ = context.get('_search_first_', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def buildcomment(comment,depth):
            return render_buildcomment(context._locals(__M_locals),comment,depth)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        maxdepth=8 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['maxdepth'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div class="w3-content" style="max-width:2000px;margin-top:46px">\n\n<table class="forum" style="margin-top: 60px;">\n\n<tr class="forum forum-odd forum-border-top">\n\t<td class="forum" style="width: 1%" rowspan=11></td>\n\t<td class="forum" style="width: 4%" rowspan=5></td>\n\t<td class="forum" style="font-size: 3em; width: 94%">\n\t\t')
        __M_writer(escape(c.page.title))
        __M_writer(u'\n\t</td>\n\t<td class="forum" style="width: 1%" rowspan=11></td>\n</tr>\n    <tr class="forum forum-odd">\n        <td class="forum" style="text-align: left; width: 5%">\n            Submitted \n            <a onmouseover="fullTime(this, \'')
        __M_writer(escape(c.page.posted.strftime('%a, %b %d %Y, %H:%M:%S %p')))
        __M_writer(u'\')" onmouseout="shortTime(this, \'')
        __M_writer(escape(c.page.posted.strftime('%a, %b %d %Y')))
        __M_writer(u'\')">\n                ')
        __M_writer(escape(c.page.posted.strftime('%a, %b %d %Y')))
        __M_writer(u'\n            </a>\n')
        if c.page.edited:
            __M_writer(u'            (last edited \n            <a onmouseover="fullTime(this, \'')
            __M_writer(escape(c.page.lastModified.strftime('%a, %b %d %Y, %H:%M:%S %p')))
            __M_writer(u'\')" \n                onmouseout="shortTime(this, \'')
            __M_writer(escape(c.page.lastModified.strftime('%a, %b %d %Y')))
            __M_writer(u'\')">\n                ')
            __M_writer(escape(c.page.lastModified.strftime('%a, %b %d %Y')))
            __M_writer(u'\n            </a>\n            ) \n')
        __M_writer(u'            by ')
        __M_writer(escape(c.page.poster))
        __M_writer(u'\n        </td>\n    </tr>\n\n    <tr class="forum forum-odd">\n    \t<td class="forum">\n    \t\t<div class = "text-post">\n    \t\t\t<p class= "text-post">')
        __M_writer(escape(c.page.content))
        __M_writer(u'</p>\n    \t\t</div>\n    \t</td>\n    </tr>\n\n    <tr class="forum forum-odd">\n        <td class="forum">')
        __M_writer(escape(len(c.page.comments)))
        __M_writer(u' comments</td>\n    </tr>\n\n    <tr class="forum forum-odd" style="margin-top: 4%; margin-bottom: 4%">\n    \t<td><br /></td>\n    </tr>\n\n    <tr class="forum forum-odd" style="padding-bottom: 3px; border-bottom: 1px solid grey">\n    \t<td class="forum" colspan=2>\n')
        if c.paginator.page != 1:
            __M_writer(u'\t    \t<a href="')
            __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.page.id) + _search_first_))
            __M_writer(u'"><<</a>\n    \t\t<a href="')
            __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.page.id) + '?page=' + str(c.paginator.page-1) + _search_))
            __M_writer(u'"><</a>\n')
        __M_writer(u'    \t\tShowing comments ')
        __M_writer(escape(c.paginator.first_item))
        __M_writer(u' through ')
        __M_writer(escape(c.paginator.last_item))
        __M_writer(u' of ')
        __M_writer(escape(c.paginator.item_count))
        __M_writer(u'\n')
        if c.paginator.page != c.paginator.last_page:
            __M_writer(u'    \t\t<a href="')
            __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.page.id) + '?page=' + str(c.paginator.page+1) + _search_))
            __M_writer(u'">></a>\n    \t\t<a href="')
            __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.page.id) + '?page=' + str(c.paginator.last_page) + _search_))
            __M_writer(u'">>></a>\n')
        __M_writer(u'\t\t</td>\n\t</tr>\n\n\t<tr class="forum forum-odd">\n\t\t<td class="forum" colspan=2>\n\t\t\t<div>\n\t\t\t\t<ul class="w3-navbar w3-grey w3-left-align" style="width: 100%;">\n  \t\t\t\t\t<li class="w3-hide-large w3-opennav w3-right">\n    \t\t\t\t\t<a class="w3-padding-large" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>\n  \t\t\t\t\t</li>\n  \t\t\t\t\t<li class="w3-hide-small w3-hide-medium" style="padding-top: 12px; padding-bottom: 12px; padding-left: 24px; padding-right: 6px">Sort By:</li>\n  \t\t\t\t\t<li id = "new" class="w3-hide-small w3-hide-medium">\n    \t\t\t\t\t<a href="')
        __M_writer(escape(h.url(controller='forums', action='view', id=c.page.id)))
        __M_writer(u'" class="w3-padding-large" style="padding-left: 6px">\n      \t\t\t\t \t\tNew\n    \t\t\t\t\t</a>\n  \t\t\t\t\t</li>\n  \t\t\t\t\t<li id="best", class="w3-hide-small w3-hide-medium">\n    \t\t\t\t\t<a href="')
        __M_writer(escape(h.url(controller='forums', action='view', id=c.page.id) + '?viewtype=best'))
        __M_writer(u'" class="w3-padding-large">\n        \t\t\t\t\tBest\n    \t\t\t\t\t</a>\n  \t\t\t\t\t</li>\n\t\t\t\t</ul>\n\t\t\t\t<script>\n\t\t\t\t\tvar active = "')
        __M_writer(escape(c.active))
        __M_writer(u'";\n\t\t\t\t\tvar activeElem = document.getElementById(active);\n\t\t\t\t\tactiveElem.className += " w3-black";\n\t\t\t\t</script>\n\t\t\t</div>\n\t\t</td>\n\t</tr>\n\n\t<tr class="forum forum-odd">\n\t\t<td class="forum" colspan=2 style="padding-top: 10px;">\n\t\t\tCommenting as ')
        __M_writer(escape(h.getUser()))
        __M_writer(u'\n\t\t</td>\n\t</tr>\n\n\t<form action="')
        __M_writer(escape(h.url(controller='forums', action='newcomment', id=c.page.id)))
        __M_writer(u'" method="post">\n\t<tr class="forum forum-odd">\n\t\t<td class="forum" colspan=2>\n\t\t\t\t<textarea id="content" name="content" rows=7 cols=60></textarea>\n\t\t\t\t\n\t\t</td>\n\t</tr>\n\t<tr class="forum forum-odd">\n\t\t<td class="forum" colspan=2 style="padding-bottom: 10px;">\n\t\t\t<input id="submit" name="submit" value="save" type="submit">\n\t\t</td>\n\t</tr>\n\n\t</form>\n\n\t<tr class="forum forum-odd">\n\t\t<td class="forum" colspan=2>\n\t\t<table class="comment">\n\t\t\t<col width="3%">\n\t\t\t<col width="94%">\n\t\t\t<col width="3%">\n')
        for comment in c.paginator:
            __M_writer(u'    \t\t')
            __M_writer(escape(buildcomment(comment, 1)))
            __M_writer(u'\n')
        __M_writer(u'\t\t</table>\n\t\t</td>\n\t</tr>\n</table>\n</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_insertSpace(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def insertSpaceBorder(_class_,border):
            return render_insertSpaceBorder(context,_class_,border)
        __M_writer = context.writer()
        __M_writer(u'\n\t')
        __M_writer(escape(insertSpaceBorder("comment-even", "")))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buildcomment(context,comment,depth):
    __M_caller = context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        h = context.get('h', UNDEFINED)
        def insertSpaceBorder(_class_,border):
            return render_insertSpaceBorder(context,_class_,border)
        len = context.get('len', UNDEFINED)
        maxdepth = context.get('maxdepth', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def buildcomment(comment,depth):
            return render_buildcomment(context,comment,depth)
        __M_writer = context.writer()
        __M_writer(u'\n\t')
        _class_ = "comment-even" if depth%2 else "comment-odd" 
        
        __M_writer(u'\n\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'" >\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-left comment-border-top")))
        __M_writer(u'\n\t\t<td class="comment comment-border-top" style="padding-top: 10px; width: 94%;">\n\t\t\t')
        __M_writer(escape(comment.uname))
        __M_writer(u' posted on\n\t\t\t<a onmouseover="fullTime(this, \'')
        __M_writer(escape(comment.created.strftime('%a, %b %d %Y, %H:%M:%S %p')))
        __M_writer(u'\')" onmouseout="shortTime(this, \'')
        __M_writer(escape(comment.created.strftime('%a, %b %d %Y')))
        __M_writer(u'\')">\n                ')
        __M_writer(escape(comment.created.strftime('%a, %b %d %Y')))
        __M_writer(u'\n            </a>\n\t\t</td>\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right comment-border-top")))
        __M_writer(u'\n\t</tr>\n\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-left")))
        __M_writer(u'\n\t\t<td class="comment" style="padding-top: 10px;">\n\t\t\t')
        __M_writer(escape(comment.content))
        __M_writer(u'\n\t\t</td>\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right")))
        __M_writer(u'\n\t</tr>\n\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-left")))
        __M_writer(u'\n\t\t<td class="comment" colspan = ')
        __M_writer(escape(2*(maxdepth-depth)+1))
        __M_writer(u' style="padding-top: 10px;">\n\t\t\t<a href="javascript:void(0)" onclick="showreply(\'')
        __M_writer(escape(comment.id))
        __M_writer(u'\')">Reply</a>\n\t\t\t<a href="javascript:void(0)" onclick="hideshow(\'')
        __M_writer(escape(comment.id))
        __M_writer(u'\')" id="')
        __M_writer(escape(comment.id))
        __M_writer(u'+">\n\t\t\t\tShow\n\t\t\t</a>\n')
        if len(comment.replies) != 1:
            __M_writer(u'\t\t\t')
            __M_writer(escape(len(comment.replies)))
            __M_writer(u' child comments\n')
        else:
            __M_writer(u'\t\t\t')
            __M_writer(escape(len(comment.replies)))
            __M_writer(u' child comment\n')
        __M_writer(u'\t\t</td>\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right")))
        __M_writer(u'\n\t</tr>\n\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'" \\>\n\t\t<td class="comment comment-border-left" colspan=2 style="padding-top: 10px; padding-left: 25px;">\n\t\t\t<a id="')
        __M_writer(escape(comment.id))
        __M_writer(u'_1" style="display: none;">Replying as ')
        __M_writer(escape(h.getUser()))
        __M_writer(u'</a>\n\t\t</td>\n\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right")))
        __M_writer(u'\n\t</tr>\n\n\t<form action="')
        __M_writer(escape(h.url(controller='forums', action='newcomment', id=c.page.id)+'?ownerid=' +str(comment.id)))
        __M_writer(u'" method="post">\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n\t\t<td class="comment comment-border-left" colspan=2 style="padding-left: 25px;">\n\t\t\t\t<textarea id="')
        __M_writer(escape(comment.id))
        __M_writer(u'_2" style="display: none;" name="content" rows=7 cols=60></textarea>\n\t\t</td>\n\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right")))
        __M_writer(u'\n\t</tr>\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n\t\t<td class="comment comment-border-left" colspan=2 style="padding-bottom: 10px; padding-left: 25px;">\n\t\t\t<input id="')
        __M_writer(escape(comment.id))
        __M_writer(u'_3" style="display: none;" name="submit" value="save" type="submit">\n\t\t\t<button id="')
        __M_writer(escape(comment.id))
        __M_writer(u'_4" type="button" href="javascript:void(0)" onclick="hidereply(\'')
        __M_writer(escape(comment.id))
        __M_writer(u'\')" style="display: none;">Cancel</button>\n\t\t</td>\n\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right")))
        __M_writer(u'\n\t</tr>\n\n\t</form>\n\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-left")))
        __M_writer(u'\n\t\t<td class="comment" style="width: 94%;">\n\t\t\t<table class="comment" id="')
        __M_writer(escape(comment.id))
        __M_writer(u'" style="display: none;">\n\t\t\t\t<col width="3%">\n\t\t\t\t<col width="94%">\n\t\t\t\t<col width="3%">\n')
        for reply in comment.replies:
            __M_writer(u'    \t\t')
            __M_writer(escape(buildcomment(reply, depth+1)))
            __M_writer(u'\n')
        __M_writer(u'\t\t\t</table>\n\t\t</td>\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right")))
        __M_writer(u'\n\t</tr>\n\n\t<tr class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u' comment-border-bottom">\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-left comment-border-bottom")))
        __M_writer(u'\n\t\t<td class="comment comment-border-bottom">\n\t\t\t<br />\n\t\t</td>\n\t\t')
        __M_writer(escape(insertSpaceBorder(_class_, "comment-border-right comment-border-bottom")))
        __M_writer(u'\n\t</tr>\n\n\t<tr class="forum forum-odd" style="border:none;">\n\t\t<td class="comment comment-border-bottom ')
        __M_writer(escape('comment-odd' if depth%2 else 'comment-even'))
        __M_writer(u'">\n\t\t<br/>\n\t\t</td>\n\t</tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_insertSpaceBorder(context,_class_,border):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n\t<td class="comment ')
        __M_writer(escape(_class_))
        __M_writer(u' ')
        __M_writer(escape(border))
        __M_writer(u'" style="width:3%"></td>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u' \n<!-- <script> -->\n\nfunction fullTime(el, modification) {\n    el.innerHTML = modification\n}\n\nfunction shortTime(el, modification) {\n    setTimeout(function () {\n        el.innerHTML = modification\n    }, 250);\n}\n\nfunction hideshow(id) {\n    var x = document.getElementById(id);\n    var plus = document.getElementById(id + "+");\n\n    if (x.style.display == \'none\') {\n    \tx.style.display = \'table\'\n    \tplus.innerHTML = "Hide"\n\n    }\n    else {\n    \tx.style.display = \'none\'\n    \tplus.innerHTML = "Show"\n    }\n}\n\nfunction showreply(id) {\n\tvar a = document.getElementById(id + "_1");\n\tvar b = document.getElementById(id + "_2");\n\tvar c = document.getElementById(id + "_3");\n\tvar d = document.getElementById(id + "_4");\n\n    a.style.display = \'table\';\n    b.style.display = \'table\';\n    c.style.display = \'inline-table\';\n    d.style.display = \'inline-table\';\n}\n\nfunction hidereply(id) {\n\tvar a = document.getElementById(id + "_1");\n\tvar b = document.getElementById(id + "_2");\n\tvar c = document.getElementById(id + "_3");\n\tvar d = document.getElementById(id + "_4");\n\n\ta.style.display = \'none\';\n    b.style.display = \'none\';\n    c.style.display = \'none\';\n    d.style.display = \'none\';\t\n\n    b.innerHTML = "";\n}\n\n')
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
{"source_encoding": "utf-8", "line_map": {"28": 0, "41": 2, "42": 3, "43": 5, "47": 5, "48": 8, "49": 12, "50": 107, "51": 117, "52": 117, "53": 124, "54": 124, "55": 124, "56": 124, "57": 125, "58": 125, "59": 127, "60": 128, "61": 129, "62": 129, "63": 130, "64": 130, "65": 131, "66": 131, "67": 135, "68": 135, "69": 135, "70": 142, "71": 142, "72": 148, "73": 148, "74": 157, "75": 158, "76": 158, "77": 158, "78": 159, "79": 159, "80": 161, "81": 161, "82": 161, "83": 161, "84": 161, "85": 161, "86": 161, "87": 162, "88": 163, "89": 163, "90": 163, "91": 164, "92": 164, "93": 166, "94": 178, "95": 178, "96": 183, "97": 183, "98": 189, "99": 189, "100": 199, "101": 199, "102": 203, "103": 203, "104": 224, "105": 225, "106": 225, "107": 225, "108": 227, "114": 10, "120": 10, "121": 11, "122": 11, "128": 14, "141": 14, "142": 15, "144": 15, "145": 17, "146": 17, "147": 18, "148": 18, "149": 20, "150": 20, "151": 21, "152": 21, "153": 21, "154": 21, "155": 22, "156": 22, "157": 25, "158": 25, "159": 28, "160": 28, "161": 29, "162": 29, "163": 31, "164": 31, "165": 33, "166": 33, "167": 36, "168": 36, "169": 37, "170": 37, "171": 38, "172": 38, "173": 39, "174": 39, "175": 40, "176": 40, "177": 40, "178": 40, "179": 43, "180": 44, "181": 44, "182": 44, "183": 45, "184": 46, "185": 46, "186": 46, "187": 48, "188": 49, "189": 49, "190": 52, "191": 52, "192": 54, "193": 54, "194": 54, "195": 54, "196": 57, "197": 57, "198": 60, "199": 60, "200": 61, "201": 61, "202": 63, "203": 63, "204": 66, "205": 66, "206": 68, "207": 68, "208": 70, "209": 70, "210": 71, "211": 71, "212": 71, "213": 71, "214": 74, "215": 74, "216": 79, "217": 79, "218": 80, "219": 80, "220": 82, "221": 82, "222": 86, "223": 87, "224": 87, "225": 87, "226": 89, "227": 91, "228": 91, "229": 94, "230": 94, "231": 95, "232": 95, "233": 99, "234": 99, "235": 103, "236": 103, "242": 6, "246": 6, "247": 7, "248": 7, "249": 7, "250": 7, "256": 234, "260": 234, "266": 3, "270": 3, "276": 270}, "uri": "forums/page.html", "filename": "/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/page.html"}
__M_END_METADATA
"""
