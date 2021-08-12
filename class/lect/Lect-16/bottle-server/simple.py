from bottle import route, run, static_file
import os

@route('/hello')
def hello():
    return "Hello World!"

@route('/')
@route('/<filename:path>')
def server_static(filename='index.html'):
    rootdir = os.path.join(os.path.dirname(__file__), 'www')
    return static_file(filename, root=rootdir)

run(host='localhost', port=9010, debug=True)

