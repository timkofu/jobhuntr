[![Coverage Status](https://coveralls.io/repos/timkofu/jobhuntr/badge.svg?branch=master&service=github)](https://coveralls.io/github/timkofu/jobhuntr?branch=master)
## Jobhuntr

#### Source code for Jobhuntr, a job search engine.

**Serving static-files in prod**: Django recommends using either [Nginx or a CDN](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/); `django-storages` in addition to enabling the use of many cloud storage backends, documents how to use [AWS S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html); this [step-by-step tutorial](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) shows how to do it all from setting up the s3 bucket to the Django configs, and [this one breaks down](https://support.cloudflare.com/hc/en-us/articles/360037983412-Configuring-an-Amazon-Web-Services-static-site-to-use-Cloudflare) how to serve up the static files in your S3 bucket from behind Cloudflare.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

![A Django Joint](https://www.djangoproject.com/m/img/badges/djangojoint107x25.gif)
