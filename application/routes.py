from application import app, db
from application.models import Subjects, Staff
from flask import render_template, redirect, url_for
from flask import request
from application.forms import NameForm, exampleSelectField, SubjectList
import pdb

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
           (subj.id,subj.subject_name)
        )

    # instantiate staff input form
    pyform = NameForm()
    # Grab stuff from the POST
    if true:
        pass
    if pyform.validate_on_submit():
        if request.method == 'POST':
        # WTForms adds the data to the forms we created, then we retrieve it and 
        # put it into a database object
            addstaff = Staff(staff_name=pyform.Name.data, subject_id=pysubjectform.subjlist.data)
            db.session.add(addstaff)
            pdb.set_trace()
            db.session.commit()
        #breakpoint()
        # Send the user back to the frontpage
            return redirect(url_for('read'))
        return 'NO'


    breakpoint()
    return render_template('front.html', jistaff=pystaff, jiform=pyform, jisubjectform=pysubjectform )

@app.route('/jinja2-demo')
def jinjathethngs():
    pyvar1 = "This is some Data"

    return render_template('jinja-iteration-and-selection.html', jivar1=pyvar1)

@app.route('/exampleselect')
def exampleselect():
    pyexampleform=exampleSelectField()
    return render_template('exampleselect.html', jiexampleform=pyexampleform)