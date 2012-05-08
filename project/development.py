
from project.settings import *
DEBUG=True
TEMPLATE_DEBUG=DEBUG

import os, sys

if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'sqlite3'}
