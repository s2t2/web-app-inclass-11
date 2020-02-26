# web-app-inclass-11

Setup from scratch:

```sh
cd /path/to/web-app-inclass-11
pipenv install
pipenv install Flask Flask-SQLAlchemy Flask-Migrate
pipenv install python-dotenv requests basilica tweepy
```

Configure .env file:

```sh
# .env

ALPHAVANTAGE_API_KEY="abc123"

BASILICA_API_KEY="__________"

TWITTER_API_KEY="__________"
TWITTER_API_SECRET="__________"
TWITTER_ACCESS_TOKEN="__________"
TWITTER_ACCESS_TOKEN_SECRET="__________"

SECRET_KEY="super secret"
DATABASE_URL="sqlite:////path/to/web-app-inclass-11/web_app_12.db"
```

Setup and migrate the database:

```sh
FLASK_APP=web_app flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the tables
```

Run the app:

```sh
FLASK_APP=web_app flask run
```
