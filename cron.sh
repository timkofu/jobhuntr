#!/usr/bin/env bash

cd /opt/code/jobhuntr/spidr
/usr/local/bin/scrapy crawl jobhuntr

/bin/sleep 1

/usr/bin/python /opt/code/jobhuntr/manage.py remove_expired
/usr/bin/yes | /usr/bin/python /opt/code/jobhuntr/manage.py rebuild_index
