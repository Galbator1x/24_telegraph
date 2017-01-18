import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

CSRF_ENABLED = True

DATABASE_URL = os.environ.get('DATABASE_URL',
                              'sqlite:///' + os.path.join(basedir, 'app.db'))
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
