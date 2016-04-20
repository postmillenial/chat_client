'''views'''
import bleach

######'''utility/common'''

def header(title=""):
    ''' i guess it's not really a header so much as a structural preamble'''

    if title is not "":
        title = bleach.clean(title) + " | "

    return '<html><head><title>' + title + 'Cat Site</title></head><body>'

def footer():
    ''' and yet 'footer' makes sense. the lack of synchronicity is something'''

    return '</body></html>'

def section(div_id, classes, text):
    '''so generic'''

    # if any of these are user data i should bleach them!!!
    div_id = bleach.clean(div_id)
    classes = bleach.clean(classes) # this may become a list or something later, just comprehens it
    text = bleach.clean(text)

    return '<div id="%s" class="%s">' % (div_id, classes) + text + '</div>'

#####'''top level pages'''

def index(environ):
    '''das is index'''
    container = section('container', '', str(environ))

    return header("Welcome") + container + footer()

def not_found():
    '''nicht faund'''
    return header("Not found!") + section
