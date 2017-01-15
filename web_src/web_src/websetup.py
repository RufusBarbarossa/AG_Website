"""Setup the web_src application"""
import logging

from web_src.config.environment import load_environment
from web_src.model.meta import Session, Base

from web_src import model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup web_src here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)

    log.info("Setting Up Categories")
    lol = model.Category()
    lol.title = u"League of Legends"

    overwatch = model.Category()
    overwatch.title = u"Overwatch"

    vain = model.Category()
    vain.title = u"Vain Glory"

    Session.add_all([lol, overwatch, vain])
    Session.commit()

    log.info("Completed Setting up Categories")

    log.info("Setting Up Forums")
    lol_forum = model.Forum()
    lol_forum.categoryid = lol.id
    lol_forum.title = u"General"
    lol_forum.sdesc = u"General Talk about League of Legends"
    lol_forum.ldesc = u""

    guide_forum = model.Forum()
    guide_forum.categoryid = lol.id
    guide_forum.title = u"Guides"
    guide_forum.sdesc = u"League of Legends Guides"
    guide_forum.ldesc = u""

    ow_forum = model.Forum()
    ow_forum.categoryid = overwatch.id
    ow_forum.title = u"General"
    ow_forum.sdesc = u"General Talk about Overwatch"
    ow_forum.ldesc = u""

    owguide_forum = model.Forum()
    owguide_forum.categoryid = overwatch.id
    owguide_forum.title = u"Guides"
    owguide_forum.sdesc = u"Owerwatch Guides"
    owguide_forum.ldesc = u""

    vain_forum = model.Forum()
    vain_forum.categoryid = vain.id
    vain_forum.title = u"General"
    vain_forum.sdesc = u"General Talk about Vain Glory"
    vain_forum.ldesc = u""

    vainguide_forum = model.Forum()
    vainguide_forum.categoryid = vain.id
    vainguide_forum.title = u"Guides"
    vainguide_forum.sdesc = u"Vain Glory Guides"
    vainguide_forum.ldesc = u""

    Session.add_all([lol_forum, guide_forum, ow_forum, owguide_forum, vain_forum, vainguide_forum])
    Session.commit()

    #For development only

    test_page = model.Page()
    test_page.title = "Testing Page"
    test_page.content = "Hi im Gosu"
    test_page.poster = "RufusBarbarossa"
    test_page.forumid = lol_forum.id
    Session.add(test_page)
    Session.commit()

    comment1 = model.Comment()
    comment1.content = "Test 1"
    comment1.uname = "RufusBarbarossa"
    comment1.pageid = test_page.id
    Session.add(comment1)
    Session.commit()

    comment2 = model.Comment()
    comment2.content = "Test 2"
    comment2.uname = "The Schiphtur"
    comment2.pageid = test_page.id
    comment2.ownerid = comment1.id
    Session.add(comment2)
    Session.commit()

    print("" + str(comment1.replies))
    print("" + str(comment1.ownerid))