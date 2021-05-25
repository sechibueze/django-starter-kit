# Python Web Development with Django

## Setup

- Install python
- Confirm python and pip installation
  - `python --version`
  - `pip --version`
- Install your IDE - VS Code or Pycharm
- Create a folder for your project
  - `mkdir <project_name>`
  - `cd <project_name>`
- Create a virtual env
  - `pip install virtualenvwrapper-win`
  - `mkvirtualenv <django>`
  - `workon <django>`
- Install django
  - `pip install django`
  - `django-admin --version`
- Create a Django project
  - `django-admin startproject <project_name>`
- Run the server
  - `python manage.py runserver`

## Workflow

- install apps => components
- configure urls.py
- setup models.py
- write a view
  - render a template
  - return data

## Migrations

- python manage.py makemigrations
- python manage.py sqlmigrate <app_name> <migration_number>
-

## Configure static assets

> create static folder for static assests
> edit settings.py

- `STATIC_URL = '/static/'`
- `STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]`
- STATIC_ROOT = os.path.join(BASE_DIR, 'assests')
- run `python manage.py collectstatic`

## Setup files uploads

## Configure admin panel

## Setup superuser

- `$ python manage.py createsuperuser`

## Deploy to heroku
