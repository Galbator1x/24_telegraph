# Telegraph Clone

Service to create anonymous articles online. Anyone can post an article and get a unique url for it.
It has the ability to edit, authentication is carried out on cookie. [Link to site.](https://telegra-ph.herokuapp.com/)

## Installation

```
$ pip install -r requirements.txt
$ . dev.env
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

## Usage

```
python manage.py runserver
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Requirements

- Python >= 3.5

## List of Heroku plugins

- heroku-config

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
