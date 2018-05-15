# Standard Library
import getpass

# Local Django
from helpinghand.settings.base import *


if getpass.getuser() in ['root']:
    from helpinghand.settings.production import *
else:
    from helpinghand.settings.staging import *
