"""
rupa's WSGI skeleton
"""

from cgi import FieldStorage
from pprint import pformat

def main(environ):
    status = '200 OK'
    headers = {'Content-Type': 'text/plain; charset=utf-8'}
    body = pformat(environ)
    return status, headers, body

class Application(object):

    def __call__(self, environ, start_response):

        def log(msg):
            print >> environ['wsgi.errors'], msg

        environ['form'] = FieldStorage(
          fp=environ['wsgi.input'],
          environ=environ.copy(),
          keep_blank_values=True
        )

        try:
            status, headers, body = main(environ)
        except Exception as ex:
            log(repr(ex))
            status = '500 Server Error'
            headers = {'Content-Type': 'text/plain; charset=utf-8'}
            body = ''

        headers['Content-Length'] = str(len(body))
        start_response(status, headers.items())
        return [body]

application = Application()
