[![Build Status](https://travis-ci.org/mwinel/myblog.svg?branch=master)](https://travis-ci.org/mwinel/myblog)

# myblog
Just a simple blog to help you express yourself. A follow up on my skillshare class.

## Stack
- Python
- Flask
- HTML
- BootsrapCSS
- CSS
- SQLite

## Create and activate virtualenv

```
python -m venv venv
venv\Scripts\activate
```

## Set enviroment variables

Update **config** and then run:

```
set FLASK_CONFIG="run.py"
```

Set a SECRET_KEY. You should set your own secure secret key for security reasons.

```
set SECRET_KEY="cut-the-bs"
```

## Requirements

```
pip install -r requirements
```

## Create DB

Create a psql databases

```
CREATE DATABASE blogger;
CREATE DATABASE blogger_test;
```

Create the tables and run the migrations:

```
flask db init
flask db migrate
flask db upgrade
```

## Run the Application

```
flask run
```

Access the application at the address **http://localhost:5000/**

## Testing

```
python manage.py test
```

## Contribute
Would you like to make **myblog** a better platform?
See [CONTRIBUTING.md](#) for the steps to contribute.

## UI
[Check out the project user interface](#)


