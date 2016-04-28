#web: newrelic-admin run-program uwsgi uwsgi.ini --enable-threads  # # Dyno will never sleep with this thing enabled/
web: uwsgi uwsgi.ini --enable-threads
#worker: celery -A jobhuntr worker -l info  # # Not yet.
