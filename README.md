Django Gulp Boilerplate v0.1
======
Author: [Yan Hong](https://ca.linkedin.com/in/yan-hong-9111073b)

What's included?
------
- [Django v1.9](https://docs.djangoproject.com/en/1.9/)
- Django base [Dockerfile](https://docs.docker.com/)
- [Gulp](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md)
- [Browsersync](https://www.browsersync.io/docs/)
- [Django Bower](https://django-bower.readthedocs.org/en/latest/usage.html)
- [Open Style UI Framework](http://hongyanh.github.io/open-style/)
- [Django Allauth](http://django-allauth.readthedocs.org/en/latest/)
- [Django Avatar](http://django-avatar.readthedocs.org/en/latest/)
- Raven (for [Sentry](https://getsentry.com/welcome/) integration)
- Postgresql connector
- Template structure
- [JQuery](http://learn.jquery.com/about-jquery/how-jquery-works/)

How to setup?
------
1. Create a key.py file under project root directory and include following attributes:
  ```Python
  # Change the values for your project settings
  # Please don't include this file in your repository

  # Project names
  PROJECT_NAME = 'your_project_name'

  # Secret keys
  DJANGO_SALT = 'your_secret_keys'

  # Database settings, by default, we use postgresql
  DB_PASSWORD = 'db_password'
  DB_NAME = 'db_name'
  DB_USER = 'db_user'
  DB_HOST = 'localhost'
  DB_PORT = ''

  # Debug mode, change it to False in production
  DEBUG = True

  # Localization settings
  LANGUAGE_CODE = 'en-us' # Your language code
  TIME_ZONE = 'America/Vancouver' # Your timezone
  ```
2. (Optional) Create a [virtualenv](https://virtualenv.readthedocs.org/en/latest/index.html) for your project
  1. Run `pip install virtualenv`
  2. CD to your project root
  3. Run `virtualenv venv`
  4. Run `source venv/bin/activate`
3. Run `pip install -r requirements.txt`
4. Run `python manage.py bower install`
5. Install [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04) and create your user and database
6. Run `python manage.py migrate`
7. Install [Gulp](https://github.com/gulpjs/gulp/blob/master/docs/getting-started.md) with [npm](https://nodejs.org/en/) `npm install -g gulp`
8. Install [SASS](http://sass-lang.com/documentation/file.SASS_REFERENCE.html) with `npm install -g jshint` and [JShint](http://jshint.com/install/) with `npm install -g jshint`
9. Run `python manage.py runserver`
10. In another terminal window, run `gulp` and it should bring up your default browser

Project Structure
------
* **/assets/** Your working static folder
  * **/img/** Put all your images in this folder
  * **/js/** Put all your JavaScript in this folder
  * **/sass/** Put all your SASS stylesheets in this folder
* **/static/** Folder generated by Gulp and you should not put static files manually in this folder
* **/main/** Django root folder. It contains settings file and homepage view, don't change the folder name
* **/templates/** HTML templates with Django templating tags

Question?
------
Email: onlyhongyan@gmail.com