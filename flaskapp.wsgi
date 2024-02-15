#!/path/to/python/env

import sys
import os
sys.path.insert(0, '/var/www/wsgi-scripts')
from flaskapp import app as application
