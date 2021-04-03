## Django Recipes App using redis cache

### Pre-requisites
[Redis](https://gist.github.com/tomysmile/1b8a321e7c58499ef9f9441b2faa0aa8)


### Setup
- Make sure redis instance is running on your machine
- Git clone the app and cd into recipes_redis
- Make a virtual env and activate it
- pip install requirements.text
- Run  `make migrate`
- Create a superuser
- Run `make start`
- Add some categories and recipes in `django-admin`
- Go to `http://localhost:8000`
