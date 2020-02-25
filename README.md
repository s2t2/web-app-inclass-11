# web-app-inclass-11


Setup from scratch:

```sh
cd /path/to/web-app-inclass-11
pipenv install
pipenv install Flask Flask-SQLAlchemy Flask-Migrate
```

Run:

```sh
FLASK_APP=app.py flask run
```

Setup and migrate the database:

```sh
FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the "users" table
```
