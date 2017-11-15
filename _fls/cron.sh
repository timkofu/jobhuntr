#!/usr/bin/env bash

python manage.py remove_expired
python manage.py spider
python manage.py update_index > /dev/null 2>&1
