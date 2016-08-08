from mages import *


@all_renderable(c.MAGES_APPS)
class Root:
    def index(self, session, message=''):
        return {
            'message': message,
            'apps': session.mages_apps()
        }

    def app(self, session, id, message='', csrf_token='', explanation=None):
        return {
            'message': message,
            'app': session.mages_application(id)
        }
