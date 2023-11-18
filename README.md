# A Basic Flask application with blueprints and tests

## Description

The application is intended to be a blueprint, a base application with all important parts set up: blueprints, tests, database, models, migration, and controllers.  

This will allow for quick project set up and will ensure that no important parts are left out when building an application.

## Instructions to run code

### Clone the repository from 
- HTTP: https://github.com/almamarie/flask_base_app_structure.git
- SSH: git@github.com:almamarie/flask_base_app_structure.git

### Install all packages;

`cd` into the project directory and run `pip install -r requirements.txt` to install all packages  
NOTE: I advise you use a virtual environment 

### run app

run `echo FLASK_APP=flaskr`  
run `echo FLASK_DEBUG=True`  
then `flask run`

## Problem

The application works well but the problem is with running tests. I am unable to import flaskr:  
running `python __init__.py` from the test file or `python tests/__init__.py` from the project directory outputs:

```{r class.source="bg-danger", class.output="bg-warning"}
Traceback (most recent call last):
  File "auth-model/tests/__init__.py", line 4, in <module>
    from test_app_init import AppInitializationTestCase
  File "/auth-model/tests/test_app_init.py", line 11, in <module>
    from flaskr import create_app
ModuleNotFoundError: No module named 'flaskr'
```

I expect that the test runs successfully.