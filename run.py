# -*- coding: utf-8 -*-

__author__ = 'maxto'
# Run a test server.
from app import app
import re


@app.template_filter('quoted')
def quoted(s):
    l = re.findall('\'([^\']*)\'', str(s))
    if l:
        return l[0]
    return None

# 'app.run' is different by os.
import sys

if sys.platform == 'win32':
    app.run(host='127.0.0.1', port=8080, debug=True)
elif sys.platform == 'linux2':
    app.run(host='0.0.0.0', port=8080, debug=True)
else:
    app.run(host='127.0.0.1', port=8080, debug=True)


