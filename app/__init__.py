import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

from app import models, views
