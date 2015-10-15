from bottle import run, route
from random import choice
from string import ascii_letters


@route("/")
def hello():
    return "hello world"

@route("/random")
def random():
    return ''.join(choice(ascii_letters) for _ in range(10))

if __name__ == '__main__':
    # the default wsgi backend doesn't play nice with p4a; cherrypi does.
    # read more at http://bottlepy.org/docs/dev/deployment.html
    run(host="0.0.0.0", port=5000, server="cherrypy")
