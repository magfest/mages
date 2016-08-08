from mages import *


@Session.model_mixin
class SessionMixin:
    def mages_apps(self):
        return self.query(MagesApplication).order_by('applied').all()


class MagesApplication(MagModel):
    event_id = Column(UUID, ForeignKey('event.id'), nullable=True)

    name = Column(UnicodeText)
    length = Column(UnicodeText)
    description = Column(UnicodeText)
    unavailable = Column(UnicodeText)
    affiliations = Column(UnicodeText)
    past_attendance = Column(UnicodeText)

    presentation = Column(Choice(c.PRESENTATION_OPTS))
    other_presentation = Column(UnicodeText)
    tech_needs = Column(MultiChoice(c.TECH_NEED_OPTS))
    other_tech_needs = Column(UnicodeText)
    panelist_bringing = Column(UnicodeText)

    applied = Column(UTCDateTime, server_default=utcnow())

    status = Column(Choice(c.PANEL_APP_STATUS_OPTS), default=c.PENDING, admin_only=True)

    applicants = relationship('MagesApplicant', backref='application')

    email_model_name = 'app'

    @property
    def email(self):
        return self.submitter and self.submitter.email

    @property
    def submitter(self):
        try:
            [submitter] = [a for a in self.applicants if a.submitter]
        except:
            return None
        else:
            return submitter

    @property
    def matching_attendees(self):
        return [a.matching_attendee for a in self.applicants if a.matching_attendee]


class MagesApplicant(MagModel):
    app_id = Column(UUID, ForeignKey('mages_application.id', ondelete='cascade'))

    submitter  = Column(Boolean, default=False)
    first_name = Column(UnicodeText)
    last_name  = Column(UnicodeText)
    email      = Column(UnicodeText)
    cellphone  = Column(UnicodeText)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @cached_property
    def matching_attendee(self):
        return self.session.query(Attendee).filter(
            func.lower(Attendee.first_name) == self.first_name.lower(),
            func.lower(Attendee.last_name) == self.last_name.lower(),
            func.lower(Attendee.email) == self.email.lower()
        ).first()
