# Flask-rest-engine

<!-- [![CircleCI](https://circleci.com/gh/TTWShell/Flask-rest-engine.svg?style=svg)](https://circleci.com/gh/TTWShell/Flask-rest-engine)
[![Documentation Status](https://readthedocs.org/projects/Flask-rest-engine/badge/?version=latest)](https://Flask-rest-engine.readthedocs.io/zh/latest/?badge=latest)
[![PyPi-Version](https://img.shields.io/pypi/v/Flask-rest-engine.svg)](https://img.shields.io/pypi/v/Flask-rest-engine.svg)
[![Python-version](https://img.shields.io/pypi/pyversions/Flask-rest-engine.svg)](https://img.shields.io/pypi/pyversions/Flask-rest-engine.svg)
[![codecov](https://codecov.io/gh/TTWShell/Flask-rest-engine/branch/master/graph/badge.svg)](https://codecov.io/gh/TTWShell/Flask-rest-engine)
[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://Flask-rest-engine.mit-license.org) -->

A flask-restful API project generator. Based on Flask-restful + SQLAlchemy + marshmallow + webargs.

This project was inspired by [Hobbit-core](https://github.com/TTWShell/hobbit-core), thanks to [@TTWShell](https://github.com/TTWShell)

<!-- # Installation

Install and update using pip(**Still using Python 2? It is time to upgrade.**):

    pip install flask-rest-engine  # install cmd

# A Simple Example

## Init project:

    flask_rest_engine --echo new -n demo -d /tmp/demo -p 5000
    cd /tmp/demo
    pipenv install -r requirements.txt && pipenv install --dev pytest pytest-cov pytest-env ipython flake8 ipdb
    pipenv shell

## Run server:

    (demo) ➜  demo FLASK_APP=app/run.py flask run
     * Serving Flask app "app/run.py"
     * Environment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

## Run test:

    (demo) ➜  demo py.test
    ===================================================== test session starts ======================================================
    platform darwin -- Python 3.7.0, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /Users/Legolas/.virtualenvs/demo-OzheZQoG/bin/python3.7
    cachedir: .pytest_cache
    rootdir: /private/tmp/demo, inifile: pytest.ini
    plugins: env-0.6.2, cov-2.7.1
    collected 2 items

    tests/test_option.py::TestOption::test_options PASSED
    tests/test_ping.py::TestAPIExample::test_ping_api PASSED

    ---------- coverage: platform darwin, python 3.7.0-final-0 -----------
    Name                         Stmts   Miss  Cover   Missing
    ----------------------------------------------------------
    app/__init__.py                  0      0   100%
    app/configs/__init__.py          0      0   100%
    app/configs/default.py           6      0   100%
    app/configs/development.py       1      1     0%   1
    app/configs/production.py        2      2     0%   1-3
    app/configs/testing.py           8      0   100%
    app/core/__init__.py             0      0   100%
    app/exts.py                      8      0   100%
    app/models/__init__.py           2      0   100%
    app/models/consts.py             1      0   100%
    app/run.py                      35      1    97%   49
    app/schemas/__init__.py          2      0   100%
    app/services/__init__.py         2      0   100%
    app/services/option.py           6      0   100%
    app/tasks/__init__.py            1      1     0%   1
    app/utils/__init__.py            0      0   100%
    app/views/__init__.py            2      0   100%
    app/views/option.py              5      0   100%
    app/views/ping.py                7      0   100%
    tests/__init__.py               17      1    94%   29
    tests/conftest.py               11      0   100%
    tests/test_option.py             5      0   100%
    tests/test_ping.py               5      0   100%
    ----------------------------------------------------------
    TOTAL                          126      6    95%


    =================================================== 2 passed in 0.24 seconds ===================================================

# Others

    flask_rest_engine --help -->