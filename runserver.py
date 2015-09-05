# -*- coding: utf-8 -*-

__author__ = 'maxto'
# Run a test server.
from app import app
from celery import Celery

# 'app.run' is different by os.
import sys

app.run(host='0.0.0.0', port=80)
