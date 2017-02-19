import os

basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = os.getenv('DEBUG', False)
CSRF_ENABLED = os.getenv('CSRF_ENABLED', True)
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI',
                                    'sqlite:///' + os.path.join(basedir, 'app.db'))
