# workflowr.io

A website to share and discover [workflowr][] projects.

[workflowr]: https://github.com/jdblischak/worklfowr

## Create a UML diagram of database schema

Use the [graph_models][] feature of [django-extensions][] to create a UML
diagram of the database schema specified in `projects/models.py`.

```
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
