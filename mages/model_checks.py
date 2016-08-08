from mages import *


MagesApplication.required = [
    ('name', 'Panel Name'),
    ('description', 'Panel Description'),
    ('length', 'Panel Length'),
    ('unavailable', 'Your unavailability'),
]
MagesApplicant.required = [
    ('first_name', 'First Name'),
    ('last_name', 'Last Name'),
    ('email', 'Email'),
]


@validation.MagesApplicant
def mages_email(ma):
    if not re.match(c.EMAIL_RE, ma.email):
        return 'Please enter a valid email address'


@validation.MagesApplicant
def mages_phone(ma):
    from uber.model_checks import _invalid_phone_number
    if (ma.submitter or ma.cellphone) and _invalid_phone_number(ma.cellphone):
        return 'Please enter a valid phone number'


@validation.MagesApplication
def mages_other(ma):
    if ma.presentation == c.OTHER and not ma.other_presentation:
        return 'Since you selected "Other" for your type of panel, please describe it'


@validation.MagesApplication
def mages_deadline(ma):
    if localized_now() > c.MAGES_APP_DEADLINE:
        return 'We are now past the deadline and are no longer accepting panel applications'
