from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app definition
app = Flask(__name__)

# config stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456789abcdefghijklmonp'


# create db class
db = SQLAlchemy(app)

# Populate the database on start if you want to use an in-memory db
#from application.createdb import populate
#populate()

from application import routes