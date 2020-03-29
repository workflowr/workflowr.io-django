# workflowr.io

A website to share and discover [workflowr][] projects.

[workflowr]: https://github.com/jdblischak/worklfowr

## Setup computational environment

The software dependencies are managed by conda and specified in
[environment.yml](environment.yml). Install [Miniconda][] to get started.

```
# Create the environment
conda env create --file environment.yml

# Activate the environment
conda activate wio

# Update the environment
conda env update --file environment.yml

# Deactivate the environment
conda deactivate wio
```

[Miniconda]: https://docs.conda.io/en/latest/miniconda.html

## Development

```
# Run the test suite
python manage.py test

# Restart database for interactive testing
bash setup-models.sh

# Create a temporary superuser for testing the site
bash createsuperuser.sh

# Run the development server (http://localhost:8000/)
python manage.py runserver

# Start an interactive shell with Django settings activated
python manage.py shell
```

## Heroku

```
# Install Heroku CLI app
sudo snap install heroku --classic

# Login (opens browser for authentication)
heroku login

# Run the development server (http://localhost:5000/)
heroku local web

# Add heroku remote
git remote add  heroku https://git.heroku.com/workflowr.git

# Deploy the site
git push heroku master

# Open the site in the browser
heroku open

# View the server logs
heroku logs --tail

# View currently used resources
heroku ps

# Start an interactive shell on the remote server
heroku run python manage.py shell

# Run the database migrations on the remote server
heroku run python manage.py migrate
```

* [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)
* [heroku/python-getting-started](https://github.com/heroku/python-getting-started)
* [Configuring Django Apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration)

## Endpoints

* `projects/` - List all projects
* `projects/github/` - List all projects hosted on GitHub
* `projects/github/user/` - List all of user's projects hosted on GitHub
* `projects/github/user/project/` - Detail view for project
* `authors/` - List all authors
* `tags/` - List all tags
* `tag/tagname/` - List all projects tagged with "tagname"
* `publications/` - List all publications

## Create a UML diagram of database schema

Use the [graph_models][] feature of [django-extensions][] to create a UML
diagram of the database schema specified in `projects/models.py`.

```
conda activate wio
python manage.py graph_models --pydot projects -o graph-model.png
```

[django-extensions]: https://django-extensions.readthedocs.io/
[graph_models]: https://django-extensions.readthedocs.io/en/latest/graph_models.html

## Resources

* [Writing your first Django app](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
* [MDN Django tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) -
[Example UML for models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
* [nomnoml R pkg for creating UML diagrams](https://github.com/javierluraschi/nomnoml)
* My [practice-django](https://github.com/jdblischak/practice-django) repo
* [djangox template](https://github.com/wsvincent/djangox)
* Authentication - [basic](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/),
[custom user](https://wsvincent.com/django-custom-user-model-tutorial/),
[allauth](https://wsvincent.com/django-allauth-tutorial/),
[custom user + allauth](https://wsvincent.com/django-allauth-tutorial-custom-user-model/)
* [Beginner's guide with tests](https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html)
* [Use slug as url parameter instead of pk](https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/#use-slug-as-url-parameter-instead-of-pk)
* [Django test client](https://docs.djangoproject.com/en/3.0/topics/testing/tools/)
