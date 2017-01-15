# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1484462468.16438
_enable_loop = True
_template_filename = '/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/viewforum.html'
_template_uri = 'forums/viewforum.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = ['scripts', 'buildrow', 'title']


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
        def buildrow(page,counter):
            return render_buildrow(context._locals(__M_locals),page,counter)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n<div class="w3-content" style="max-width:2000px;margin-top:46px">\n\n<h1 style="text-align: center">')
        __M_writer(escape(c.forum.title))
        __M_writer(u'</h1>\n\n<p style="text-align: center">')
        __M_writer(escape(c.forum.sdesc))
        __M_writer(u'</p>\n\n\n')
        if c.empty and c.search_text == '':
            __M_writer(u'<br /> <br />\n<p style="font-size: 2.5em; text-align: center"> There are no threads in this forum. Contribute by creating a thread <a href="')
            __M_writer(escape('' + h.url(controller='forums', action='new') + '?forumid=' + str(c.forum.id)))
            __M_writer(u'">here</a></p>\n')
        else:
            __M_writer(u'<div>\n<ul class="w3-navbar w3-grey w3-left-align" style="margin-left: 2%; width: 96%;">\n  <li class="w3-hide-large w3-opennav w3-right">\n    <a class="w3-padding-large" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>\n  </li>\n  <li class="w3-hide-small w3-hide-medium"><a href="')
            __M_writer(escape(h.url(controller='forums', action='new') + '?forumid=' + str(c.forum.id)))
            __M_writer(u'" class="w3-padding-large">New Thread</a></li>\n  <li class="w3-hide-small w3-hide-medium" style="padding-top: 12px; padding-bottom: 12px; padding-left: 24px; padding-right: 6px">Sort By:</li>\n  <li id = "new" class="w3-hide-small w3-hide-medium">\n    <a href="')
            __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id)))
            __M_writer(u'" class="w3-padding-large" style="padding-left: 6px">\n        New\n    </a>\n  </li>\n  <li id="best", class="w3-hide-small w3-hide-medium">\n    <a href="')
            __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?viewtype=best'))
            __M_writer(u'" class="w3-padding-large">\n        Best\n    </a>\n  </li>\n  <li class="w3-hide-small w3-hide-medium w3-right">\n    <form>\n        <input class="searchbar" type="text" name="search" placeholder="')
            __M_writer(escape('Search..' if c.search_text == '' else c.search_text))
            __M_writer(u'">\n    </form>\n   </li>\n</ul>\n<script>\n\nvar active = "')
            __M_writer(escape(c.active))
            __M_writer(u'";\nvar activeElem = document.getElementById(active);\nactiveElem.className += " w3-black";\n\n</script>\n\n</div>\n')
            if not c.empty:
                __M_writer(u'<div>\n<table class="paginator forum">\n')
                counter=0 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                for page in c.paginator:
                    __M_writer(u'\t')
                    counter += 1 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['counter'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n    ')
                    __M_writer(escape(buildrow(page, counter)))
                    __M_writer(u'\n')
                __M_writer(u'</table>\n\n')
                _search_first_ = '' if c.search_text == '' else '?search='+c.search_text 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_search_first_'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                _search_ = '' if c.search_text == '' else '&search='+c.search_text 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_search_'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n\n<p style="margin-left:3%">\n')
                if c.paginator.page != 1:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + _search_first_))
                    __M_writer(u'"><<</a>\n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page-1) + _search_))
                    __M_writer(u'"><</a>\n')
                __M_writer(u'    Showing threads ')
                __M_writer(escape(c.paginator.first_item))
                __M_writer(u' through ')
                __M_writer(escape(c.paginator.last_item))
                __M_writer(u' of ')
                __M_writer(escape(c.paginator.item_count))
                __M_writer(u'\n')
                if c.paginator.page != c.paginator.last_page:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page+1) + _search_))
                    __M_writer(u'">></a>\n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.last_page) + _search_))
                    __M_writer(u'">>></a>\n')
                __M_writer(u'</p>\n\n<p style="margin-left:3%">\n\n')
                if c.paginator.page == 1:
                    __M_writer(u'    <!-- Do Nothing -->\n')
                elif c.paginator.page == 2:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=1' + _search_))
                    __M_writer(u'">1</a> \n')
                elif c.paginator.page == 3:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=1' + _search_))
                    __M_writer(u'">1</a> \n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=2' + _search_))
                    __M_writer(u'">2</a> \n')
                else:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=1' + _search_))
                    __M_writer(u'">1</a> .. \n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page-2) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.page-2))
                    __M_writer(u'</a> \n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page-1) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.page-1))
                    __M_writer(u'</a> \n')
                __M_writer(u'\n    <a href="')
                __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page) + _search_))
                __M_writer(u'">[')
                __M_writer(escape(c.paginator.page))
                __M_writer(u']</a> \n\n')
                if c.paginator.page == c.paginator.last_page:
                    __M_writer(u'    <!-- Do Nothing -->\n')
                elif c.paginator.page == c.paginator.last_page - 1:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.last_page) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.last_page))
                    __M_writer(u'</a>\n')
                elif c.paginator.page == c.paginator.last_page - 2:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.last_page-1) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.last_page-1))
                    __M_writer(u'</a> \n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.last_page) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.last_page))
                    __M_writer(u'</a>\n')
                else:
                    __M_writer(u'    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page+1) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.page+1))
                    __M_writer(u'</a> \n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.page+2) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.page+2))
                    __M_writer(u'</a> .. \n    <a href="')
                    __M_writer(escape(h.url(controller='forums', action='viewforum', id=c.forum.id) + '?page=' + str(c.paginator.last_page) + _search_))
                    __M_writer(u'">')
                    __M_writer(escape(c.paginator.last_page))
                    __M_writer(u'</a>\n')
                __M_writer(u'\n</p>\n</div>\n')
        __M_writer(u'</div>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u' \n<!-- <script> -->\n\nfunction fullTime(el, modification) {\n    el.innerHTML = modification\n}\n\nfunction shortTime(el, modification) {\n    setTimeout(function () {\n        el.innerHTML = modification\n    }, 250);\n}\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_buildrow(context,page,counter):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        _class_ = "forum-even" if counter%2 == 0 else "forum-odd" 
        
        __M_writer(u'\n    ')
        _first_ = "forum-border-top" if counter==1 else "" 
        
        __M_writer(u'\n\n    <tr class="forum ')
        __M_writer(escape(_class_))
        __M_writer(u' ')
        __M_writer(escape(_first_))
        __M_writer(u'">\n        <td class="forum" style="width: 5%" rowspan=3></td>\n        <td class="forum" style="width: 95%">\n            <a class="threadlink", href="')
        __M_writer(escape(h.url(controller='forums', action='view', id=page.id)))
        __M_writer(u'">')
        __M_writer(escape(page.title))
        __M_writer(u'</a>\n        </td>\n    </tr>\n    <tr class="forum ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n        <td class="forum" style="text-align: left; width: 5%">\n            Submitted \n            <a onmouseover="fullTime(this, \'')
        __M_writer(escape(page.posted.strftime('%a, %b %d %Y, %H:%M:%S %p')))
        __M_writer(u'\')" onmouseout="shortTime(this, \'')
        __M_writer(escape(page.posted.strftime('%a, %b %d %Y')))
        __M_writer(u'\')">\n                ')
        __M_writer(escape(page.posted.strftime('%a, %b %d %Y')))
        __M_writer(u'\n            </a>\n')
        if page.edited:
            __M_writer(u'            (last edited \n            <a onmouseover="fullTime(this, \'')
            __M_writer(escape(page.lastModified.strftime('%a, %b %d %Y, %H:%M:%S %p')))
            __M_writer(u'\')" \n                onmouseout="shortTime(this, \'')
            __M_writer(escape(page.lastModified.strftime('%a, %b %d %Y')))
            __M_writer(u'\')">\n                ')
            __M_writer(escape(page.lastModified.strftime('%a, %b %d %Y')))
            __M_writer(u'\n            </a>\n            ) \n')
        __M_writer(u'            by ')
        __M_writer(escape(page.poster))
        __M_writer(u'</td>\n    </tr>\n    <tr class="forum forum-border-bottom ')
        __M_writer(escape(_class_))
        __M_writer(u'">\n        <td class="forum">')
        __M_writer(escape(len(page.comments)))
        __M_writer(u' comments</td>\n    </tr>\n')
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
{"source_encoding": "utf-8", "line_map": {"28": 0, "38": 2, "39": 3, "40": 34, "41": 38, "42": 38, "43": 40, "44": 40, "45": 43, "46": 44, "47": 45, "48": 45, "49": 46, "50": 47, "51": 52, "52": 52, "53": 55, "54": 55, "55": 60, "56": 60, "57": 66, "58": 66, "59": 72, "60": 72, "61": 79, "62": 80, "63": 82, "67": 82, "68": 83, "69": 84, "70": 84, "74": 84, "75": 85, "76": 85, "77": 87, "78": 89, "82": 89, "83": 90, "87": 90, "88": 93, "89": 94, "90": 94, "91": 94, "92": 95, "93": 95, "94": 97, "95": 97, "96": 97, "97": 97, "98": 97, "99": 97, "100": 97, "101": 98, "102": 99, "103": 99, "104": 99, "105": 100, "106": 100, "107": 102, "108": 106, "109": 107, "110": 108, "111": 109, "112": 109, "113": 109, "114": 110, "115": 111, "116": 111, "117": 111, "118": 112, "119": 112, "120": 113, "121": 114, "122": 114, "123": 114, "124": 115, "125": 115, "126": 115, "127": 115, "128": 116, "129": 116, "130": 116, "131": 116, "132": 118, "133": 119, "134": 119, "135": 119, "136": 119, "137": 121, "138": 122, "139": 123, "140": 124, "141": 124, "142": 124, "143": 124, "144": 124, "145": 125, "146": 126, "147": 126, "148": 126, "149": 126, "150": 126, "151": 127, "152": 127, "153": 127, "154": 127, "155": 128, "156": 129, "157": 129, "158": 129, "159": 129, "160": 129, "161": 130, "162": 130, "163": 130, "164": 130, "165": 131, "166": 131, "167": 131, "168": 131, "169": 133, "170": 138, "176": 141, "180": 141, "186": 5, "192": 5, "193": 6, "195": 6, "196": 7, "198": 7, "199": 9, "200": 9, "201": 9, "202": 9, "203": 12, "204": 12, "205": 12, "206": 12, "207": 15, "208": 15, "209": 18, "210": 18, "211": 18, "212": 18, "213": 19, "214": 19, "215": 21, "216": 22, "217": 23, "218": 23, "219": 24, "220": 24, "221": 25, "222": 25, "223": 29, "224": 29, "225": 29, "226": 31, "227": 31, "228": 32, "229": 32, "235": 3, "239": 3, "245": 239}, "uri": "forums/viewforum.html", "filename": "/home/astanesc/Documents/AG_Web/AG_Website/web_src/web_src/templates/forums/viewforum.html"}
__M_END_METADATA
"""
