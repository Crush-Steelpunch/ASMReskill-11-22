from application import app, db
from application.models import Subjects, Staff
from flask import render_template



@app.route('/', methods = ['GET'])
def read():
#    pystaff = Staff.query.join(Subjects).first()
    return render_template('disclaimer.html')

