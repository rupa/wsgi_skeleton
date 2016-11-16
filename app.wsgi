import os
import sys

sys.path.append(os.path.dirname(__file__))

from wsgi_app import WSGIApp


application = WSGIApp()
