# -*- coding: utf-8 -*-

__author__ = 'maxto'
# Run a test server.
from app import app
from celery import Celery

# 'app.run' is different by os.
import sys
if __name__ == '__main__':
	if sys.platform == 'win32':
	    app.run(host='127.0.0.1', port=8080, debug=True)
	elif sys.platform == 'linux2':
	    app.run(host='0.0.0.0', port=8080, debug=True)


