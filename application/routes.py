from application import app, db
from application.models import Subjects, Staff
from flask import render_template



@app.route('/', methods = ['GET'])
def read():
    pystaff = Staff.query.join(Subjects).first()
    breakpoint()
    return render_template('front.html', jistaff=pystaff )

@app.route('/jinja2-demo')
def jinjathethngs():
    pyvar1 = "This is some Data"
    return render_template('jinja-iteration-and-selection.html', jivar1=pyvar1)