# Setup

### Setup virtual environment -
#### Install virtualenv
```sh
$ pip install --user virtualenv
```
#### Create a virtual environment
```sh
$ python -m venv venv
```
#### Activate the environment
```sh
$ source venv/bin/activate
```
#### Install all dependencies
```sh
$ pip install -r requirements/requirements.txt
```

### Setup django

#### Setup database
This project is using SQLite dabase, user can change dabase type in activity/setting.py and setup accordingly.

```sh
$ cd activity
$ python manage.py makemigrations
$ python manage.py migrate
```

#### Create superuser

```sh
$ python manage.py createsuperuser
```


#### Run server
```sh
$ python manage.py runserver
```

