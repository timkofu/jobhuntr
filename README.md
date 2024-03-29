[![Coverage Status](https://coveralls.io/repos/timkofu/jobhuntr/badge.svg?branch=main&service=github)](https://coveralls.io/github/timkofu/jobhuntr?branch=main)
## Jobhuntr

#### Source code for Jobhuntr, a job search engine.

**Serving static-files in prod**: Django recommends using either [Nginx or a CDN](https://docs.djangoproject.com/en/4.0/howto/static-files/deployment/); `django-storages` shows how to store your static files in [AWS S3](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html); this [step-by-step tutorial](https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/) shows how to do it all from setting up the S3 bucket to the Django configs (remember to set [CORS headers on your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html?icmpid=docs_s3_hp_cors_editor_page)), and [this one breaks down](https://support.cloudflare.com/hc/en-us/articles/360037983412-Configuring-an-Amazon-Web-Services-static-site-to-use-Cloudflare) how to serve up said static files from behind Cloudflare.

[![A Django Joint](https://www.djangoproject.com/m/img/badges/djangojoint107x25.gif)](https://www.djangoproject.com/)
