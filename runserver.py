# -*- coding: utf-8 -*-

__author__ = 'maxto'
# Run a test server.
from app import app as application

# 'app.run' is different by os.

application.run(host='127.0.0.1', port=8080)
