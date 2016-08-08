from mages import *

AutomatedEmail.extra_models[MagesApplication] = lambda session: session.query(MagesApplication).all()


class MagesAppEmail(AutomatedEmail):
    def __init__(self, *args, **kwargs):
        if len(args) < 3 and 'filter' not in kwargs:
            kwargs['filter'] = lambda x: True
        AutomatedEmail.__init__(self, MagesApplication, *args, sender=c.MAGES_EMAIL, **kwargs)

MagesAppEmail('Your {EVENT_NAME} MAGES Application Has Been Received', 'mages_app_confirmation.txt')
