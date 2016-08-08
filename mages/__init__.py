from uber.common import *
from mages._version import __version__
from mages.config import *
from mages.models import *
import mages.model_checks
from mages.automated_emails import *

static_overrides(join(mages_config['module_root'], 'static'))
template_overrides(join(mages_config['module_root'], 'templates'))
mount_site_sections(mages_config['module_root'])
