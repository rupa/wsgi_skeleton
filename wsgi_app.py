from cgi import FieldStorage
from pprint import pformat


class WSGIApp(object):
    """
    WSGI boilerplate. Includes form.
    """

    def process_request(self, environ):
        """
        Override me!
        """
        return ('200 OK', {}, pformat(environ))

    def _response(self, status, headers, data, start_response):
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'text/plain; charset=utf-8'
        headers['Content-Length'] = str(len(data))
        start_response(status, headers.items())
        return [data]

    def __call__(self, environ, start_response):
        environ['form'] = FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ.copy(),
            keep_blank_values=True
        )
        status, headers, data = self.process_request(environ)
        return self._response(status, headers, data, start_response)
