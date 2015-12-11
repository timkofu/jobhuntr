#!/usr/bin/env bash

cd /opt/code/jobhuntr/spidr
/opt/anaconda2/bin/scrapy crawl jobhuntr

/opt/anaconda2/bin/python /opt/code/jobhuntr/manage.py remove_expired

# email error only if stderr is written to
/opt/anaconda2/bin/python /opt/code/jobhuntr/manage.py rebuild_index --noinput > /dev/null
