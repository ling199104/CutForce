# !usr/bin/env python3
# _*_ coding: utf-8 _*_

from apis.templates.__init__ import *


@app.route("/")
def index():
    return 'Please login~'


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
