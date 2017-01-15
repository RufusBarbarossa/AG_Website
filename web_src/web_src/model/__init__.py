"""The application's model objects"""
from web_src.model.meta import Session, Base

import sqlalchemy as sa
from sqlalchemy import orm

import datetime
from sqlalchemy import schema, types

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

def now():
	return datetime.datetime.now()

category_table = schema.Table('category', Base.metadata,
	schema.Column('id', types.Integer,
		schema.Sequence('category_seq_id', optional=True), primary_key=True),
	schema.Column('title', types.Unicode(255), nullable=False),
)

forum_table = schema.Table('forum', Base.metadata,
	schema.Column('id', types.Integer,
		schema.Sequence('forum_seq_id', optional=True), primary_key=True),
	schema.Column('categoryid', types.Integer,
        schema.ForeignKey('category.id'), nullable=False),
	schema.Column('title', types.Unicode(255), nullable=False),
	schema.Column('sdesc', types.Unicode(255), nullable=False),
	schema.Column('ldesc', types.Text(), default=u''),
)

page_table = schema.Table('page', Base.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('page_seq_id', optional=True), primary_key=True),
    schema.Column('forumid', types.Integer,
        schema.ForeignKey('forum.id'), nullable=False),
    schema.Column('content', types.Text(), nullable=False),
    schema.Column('posted', types.DateTime(), default=now()),
    schema.Column('edited', types.Boolean(), default=False),
    schema.Column('lastModified', types.DateTime(), default=now()),
    schema.Column('poster', types.Unicode(255), nullable=False),
    schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
    schema.Column('upvotes', types.Integer, default=0),
)

comment_table = schema.Table('comment', Base.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('comment_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer,
        schema.ForeignKey('page.id'), nullable=False),
    schema.Column('ownerid', types.Integer,
    	schema.ForeignKey('comment.id'), nullable=True),
    schema.Column('content', types.Text(), default=u''),
    schema.Column('uname', types.Unicode(255), nullable=False),
    schema.Column('created', types.TIMESTAMP(), default=now()),
    schema.Column('upvotes', types.Integer, default=0),
)

pagetag_table = schema.Table('pagetag', Base.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('page.id')),
    schema.Column('tagid', types.Integer, schema.ForeignKey('tag.id')),
)

tag_table = schema.Table('tag', Base.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('tag_seq_id', optional=True), primary_key=True),
    schema.Column('name', types.Unicode(20), nullable=False, unique=True),
)

class Category(object):
	pass

class Forum(object):
	pass

class Page(object):
    pass

class Comment(object):
    pass

class Tag(object):
    pass

orm.mapper(Comment, comment_table, properties={
	'replies':orm.relation(Comment)
})
orm.mapper(Tag, tag_table)
orm.mapper(Page, page_table, properties={
   'comments':orm.relation(Comment, backref='page'),
   'tags':orm.relation(Tag, secondary=pagetag_table)
})
orm.mapper(Forum, forum_table, properties={
	'pages':orm.relation(Page, backref='forum')
})
orm.mapper(Category, category_table, properties={
	'forums':orm.relation(Forum, backref='category')
})