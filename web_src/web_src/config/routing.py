"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = True
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('/login', controller='userinfo', action='login')   
    map.connect('/settings', controller='userinfo', action='user_settings')
    map.connect('/logout', controller='userinfo', action='logout')
    map.connect('/register', controller='userinfo', action='register')
    map.connect('/notifications', controller='userinfo', action='notifs')
    map.connect('/settings/{action}', controller='userinfo')
    map.connect('/notifications/{action}', controller='userinfo')


    map.connect('/forums', controller='forums', actions='index')

    map.connect('/', controller='index', action='home')
    map.connect('/{action}', controller='index')

    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')

    return map
