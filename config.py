import os

basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = os.environ.get('DEBUG', False)
CSRF_ENABLED = os.environ.get('CSRF_ENABLED', True)
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                         'sqlite:///' + os.path.join(basedir, 'app.db'))
