import logging

import web_src.lib.helpers as h
import web_src.model as model
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from web_src.lib.base import BaseController, render

import formencode
from formencode import htmlfill
from pylons.decorators import validate
from pylons.decorators.rest import restrict
import webhelpers.paginate as paginate



log = logging.getLogger(__name__)

class NewPageForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter some content for the page.'
        }
    )
    forumid = formencode.validators.Int(not_empty=True)
    title = formencode.validators.String(not_empty=True)

class NewCommentForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(not_empty=True)

class ForumsController(BaseController):

    def index(self):
        category_q = model.Session.query(model.Category)
        c.categories = category_q.all()    	

        return render("forums/index.html")

    def view(self, id):
        page_q = model.Session.query(model.Page).filter_by(id=id)

        if len(page_q.all()) == 0:
            abort(404)

        c.page = page_q.first()
        comment_q = model.Session.query(model.Comment).filter_by(pageid=id)
        c.comments = comment_q.all()

        c.top_comments = comment_q.filter_by(ownerid=None).order_by(model.comment_table.c.created.desc()).all()

        c.paginator = paginate.Page(
            c.top_comments,
            page=int(request.params.get('page', 1)),
            items_per_page = 10,
        )

        c.active = request.params.get('viewtype', 'new')


        return render("forums/page.html")

    def viewforum(self, id):
        forum_q = model.Session.query(model.Forum).filter_by(id=id)
        if len(forum_q.all()) == 0:
            abort(404)

        c.forum = forum_q.first()
        
        thread_q = model.Session.query(model.Page).filter_by(forumid=id)

        #search
        c.search_text = request.params.get('search', '')
        if not c.search_text == '':
            thread_q = thread_q.filter(model.page_table.c.title.like(u'%' + c.search_text + u'%'))

        thread_q = thread_q.order_by(model.page_table.c.posted.desc())

        c.paginator = paginate.Page(
            thread_q.all(),
            page=int(request.params.get('page', 1)),
            items_per_page = 10,
        )

        c.empty = False
        if len(thread_q.all()) == 0:
            c.empty = True

        c.active = request.params.get('viewtype', 'new')

        return render("forums/viewforum.html")

    def new(self):
        c.forumid = request.params.get('forumid', '')
        return render('/forums/new.html')

    @restrict('POST')
    @validate(schema=NewCommentForm, form='view')
    def newcomment(self, id):
        comment = model.Comment()
        for k,v in self.form_result.items():
            print("k,v" + str(k) + " " + str(v))
            comment.content = v

        comment.uname = h.getUser();
        comment.created = model.now();
        comment.pageid = id;
        comment.ownerid = request.params.get('ownerid', None)

        model.Session.add(comment)
        model.Session.commit()

        redirect(url(controller='forums', action='view', id=id))
        return "kek"

    @restrict('POST')
    @validate(schema=NewPageForm, form='new')
    def create(self):
        page = model.Page()
        forumid = -1
        for k, v in self.form_result.items():
            setattr(page, k, v)
            if(k == "forumid"):
                forumid = v

        page.poster = h.getUser();
        page.posted = model.now();
        page.lastModified = model.now();

        model.Session.add(page)
        model.Session.commit()

        redirect(url(controller='forums', action='viewforum', id=forumid))
        return "kek"
