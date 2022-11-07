from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# app definition
app = Flask(__name__)

# config stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leon.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create db class
db = SQLAlchemy(app)

from application import routes