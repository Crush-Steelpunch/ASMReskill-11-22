from application import app, db
from application.models import Subjects, Staff
from flask import render_template
from flask import request
from application.forms import NameForm, exampleSelectField, SubjectList

@app.route('/', methods = ['GET','POST'])
def read():
    # query list of staff from db
    pystaff = Staff.query.join(Subjects).all()
    # query subjects
    pysubjects = Subjects.query.all()
    # instantiate empty subject form
    pysubjectform = SubjectList()
    # append query to choices
    for subj in pysubjects:
        pysubjectform.subjlist.choices.append(
           subj.subject_name
        )

    # instantiate staff input form
    pyform = NameForm()
    if request.method == 'POST':
        addstaff = Staff(staff_name=pyform.Name.data, subject_id=pyform.subjid.data)
        db.session.add(addstaff)
        db.session.commit()
        #breakpoint()


#    breakpoint()
    return render_template('front.html', jistaff=pystaff, jiform=pyform, jisubjectform=pysubjectform )

@app.route('/jinja2-demo')
def jinjathethngs():
    pyvar1 = "This is some Data"

    return render_template('jinja-iteration-and-selection.html', jivar1=pyvar1)

@app.route('/exampleselect')
def exampleselect():
    pyexampleform=exampleSelectField()
    return render_template('exampleselect.html', jiexampleform=pyexampleform)