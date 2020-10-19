#!/bin/sh
flask db upgrade
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - faq:app