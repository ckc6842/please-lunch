# -*- coding: utf-8 -*-

__author__ = 'maxto'
# Run a test server.
from app import app as application
from celery import Celery

# 'app.run' is different by os.
import sys

if __name == "__main_":
	application.run(host='0.0.0.0')
