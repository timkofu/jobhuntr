#!/usr/bin/env bash

cd /opt/code/jobhuntr/spidr
/opt/anaconda2/bin/scrapy crawl jobhuntr

/bin/sleep 1

/opt/anaconda2/bin/python /opt/code/jobhuntr/manage.py remove_expired
/usr/bin/yes | /opt/anaconda2/bin/python /opt/code/jobhuntr/manage.py rebuild_index
