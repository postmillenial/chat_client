'''
returns a webpage
'''
#from wsgiref.simple_server import make_server
import datetime
#try:
from urlparse import parse_qs
#except:
#from six.moves.urllib.parse import parse_qs
import pages
#import bleach

#bleach.clean(content)
# the wsgi interface requires a function
# that i guess takes an environment,
# a callback to actually deliver the headers
# and ones it creates the data for the headers
# calls that start_response callback.
#
# it returns an iterator on the data dict.
def app(environ, start_response):
    '''App object'''

    ## environ is a dict of environment variables
    # gunicorn theoretically can handle auth?? MEHHH

    # parse_qs returns a dict from the query string
    queryd = parse_qs(environ['QUERY_STRING'])
    print queryd
    #wtf why can't gunicorn/wsgi take a unicode string list

    data = pages.index(queryd).encode('utf-8')  # construct the page

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html; charset=utf-8'),
        ('Content-length', str(len(data)))
    ]
    start_response(status, response_headers)

    return iter([data])


def main():
    '''sorry this is an app server'''

    print "nah"

if __name__ == '__main__':
    main()
