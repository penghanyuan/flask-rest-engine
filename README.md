# Flask-rest-engine

<!-- [![CircleCI](https://circleci.com/gh/TTWShell/Flask-rest-engine.svg?style=svg)](https://circleci.com/gh/TTWShell/Flask-rest-engine)
[![Documentation Status](https://readthedocs.org/projects/Flask-rest-engine/badge/?version=latest)](https://Flask-rest-engine.readthedocs.io/zh/latest/?badge=latest)
[![PyPi-Version](https://img.shields.io/pypi/v/Flask-rest-engine.svg)](https://img.shields.io/pypi/v/Flask-rest-engine.svg)
[![Python-version](https://img.shields.io/pypi/pyversions/Flask-rest-engine.svg)](https://img.shields.io/pypi/pyversions/Flask-rest-engine.svg)
[![codecov](https://codecov.io/gh/TTWShell/Flask-rest-engine/branch/master/graph/badge.svg)](https://codecov.io/gh/TTWShell/Flask-rest-engine)
[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://Flask-rest-engine.mit-license.org) -->

A flask-restful API project generator. Based on Flask-restful + SQLAlchemy + marshmallow + webargs.

This project was inspired by [Hobbit-core](https://github.com/TTWShell/hobbit-core), thanks to [@TTWShell](https://github.com/TTWShell)

## Installation

Install and update using pip:

    pip install flask-rest-engine  # install cmd

## Init project

    flask_rest_engine --echo new -n demo -d /tmp/demo -p 5000
    cd /tmp/demo
    pipenv install -r requirements.txt
    pipenv shell

## Run server

    (demo) ➜  demo FLASK_APP=app/run.py flask run
     * Serving Flask app "app/run.py"
     * Environment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Project structure

    .
    ├── Dockerfile
    ├── app
    │   ├── __init__.py
    │   ├── configs
    │   │   ├── __init__.py
    │   │   ├── default.py
    │   │   ├── development.py
    │   │   ├── logger_config.py
    │   │   ├── production.py
    │   │   └── testing.py
    │   ├── core
    │   │   └── __init__.py
    │   ├── exts.py
    │   ├── models
    │   │   └── __init__.py
    │   ├── run.py
    │   ├── schemas
    │   │   └── __init__.py
    │   ├── tasks
    │   │   └── __init__.py
    │   ├── utils
    │   │   └── __init__.py
    │   └── endpoints
    │       ├── __init__.py
    │       └── ping.py
    ├── configs
    │   └── gunicorn-logging.ini
    ├── deploy.sh
    ├── docker-compose.yml
    ├── docs
    │   └── index.apib
    ├── pytest.ini
    ├── requirements.txt
    └── tests
        ├── __init__.py
        ├── conftest.py
        └── test_tools.py

### app

App dir saved all business layer codes. You must ensure dir name is app based on *convention over configuration*.

app.exts.py

To avoid circular imports in Flask and flask extention, exts.py used. [Why use exts.py to instance extension](https://stackoverflow.com/questions/42909816/can-i-avoid-circular-imports-in-flask-and-sqlalchemy/51739367#51739367)

app.run.py

#### app.configs

In a hobbit app, we auto load config by FLASK_ENV. If FLASK_ENV=production, used ``configs/production.py`` file.

#### app.core

All complicated function, base class etc.

#### app.models

Create your models here.

#### app.schemas

Create your marshmallow scheams here.

#### app.tasks

Celery tasks here.

#### app.utils

All common utils here.

#### app.endpoints

Create your views here.

### deploy.sh

A script for deploy.

### docker-compose.yml

Base docker compose file. Run app

    docker-compose up

### docs

API doc etc.

### logs

All logs for app, nginx etc.

### tests

Create your tests here. Recommended use [pytest](https://docs.pytest.org/en/latest/)

## Dockerfile

Build image for run web server. For more information about dockerfile, please visit : [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#usage)
