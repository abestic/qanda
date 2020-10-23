# Qanda
A simple Q&amp;A platform

## Overview

### Purpose

Qanda aims to provide a central respository of questions matched to possible answers to those questions.  Questions can have more than one answer, and answers can be up- or down-voted by a community of users.

## Contributing

Propose your change in an issue, or directly create a pull request with your improvements.

### Running the App locally with Flask

After cloning this repository, you can test-drive (and contribute to) the app locally with python and Flask.

* Setup a virtual environment of this project: `python -m venv venv`
* Enter the virtual environment: `source /venv/bin/activate`
* Install dependencies: `pip install -r requirements.txt`
* Initialize the database: `flask db upgrade`
* Start the application: `flask run`

### Working with Resource-Based Routing

Resource-based routing mapps HTTP verbs & route paths to Flask view functions (endpoints).  This results in predictable URL patternst hat are intuitive to users, and keeps view functions focused on doing only one thing at a time.

| HTTP Verb | Path                 | Endpoint   | Description                                              |
| --------- | -------------------- | ---------- | -------------------------------------------------------- |
| GET       | /objects             | index()    | display a list of all objects                            |
| GET       | /objects/new         | new()      | display a form for creating a new object                 |
| POST      | /objects             | create()   | create a new object in the database                      |
| GET       | /objects/(id)        | show()     | display an object, specified by an id                    |
| GET       | /objects/(id)/edit   | edit()     | display a form for editing an object, specified by an id |
| POST      | /objects/(id)        | update()   | update an object, specified by an id                     |
| POST      | /objects/(id)/delete | delete()   | delete an object, specified by an id                     |

**Note:** (id) is a variable component of the path

### Working with the Database

Qanda uses the [Flask-SQLAlchemy](http://flask-sqlalchemy.palletsprojects.com) library to handle database migrations, as well as communication with the database.  The application will default to use a SQLite database if a `SQLALCHEMY_DATABASE_URI` environment variable is **not** present.  The application is designed to work with a MySQL database in a production environment.  You can learn more about SQL-Alchemy and supported databases [here](http://www.sqlalchemy.org).

After making changes to models.py, run the following comand to generate a database migration:

``` sh
flask db migrate -m "migration description"
```

To initialize, or update, the database with new migrations, run:

``` sh
flask db upgrade
```

### Working with Elasticsearch

Quanda uses [Elasticsearch](https://www.elastic.co/elasticsearch) to provide search functionality.  The application will look for a `ELASTICSEARCH_URL` environment variable to connect to an Elasticsearch instance.  If no variable is present, the app will ignore Elasticsearch and continue to function without a search feature (ie: for unit testing).

To work with search in a local environment:

* Download Elasticsearch from docker hub: `docker pull elasticsearch:7.9.2` (you must include a tag)
* Run the Elasticsearch container locally: `docker run --name elasticsearch -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" --rm elasticsearch:7.9.2`
* You can test that Elasticsearch is running by hitting `http://localhost:9200` in your browser (you will see a json object describing the Elasticsearch instance if it is running properly)
* Add `ELASTICSEARCH_URL=http://localhost:9200` to a `.flaskenv` file in your local repo
* Run the app: `flask run`

To add test data to the Elasticsearch index:

* Launch a flask shell: `flask shell`
* Run the reindex method on the Question model: `Question.reindex()`
