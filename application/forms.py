from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField

# Form definitions for web input

class NameForm(FlaskForm):
    Name = StringField("StaffName", validators=[])
    subjid = StringField("SubjectId")
    submit = SubmitField("Submit")

class SubjectList(FlaskForm):
    subjlist = SelectField("Subject List", choices=[])
    submit = SubmitField("Submit")


class exampleSelectField(FlaskForm):
    list = SelectField("Farm Animals", choices=['cows','chickens','geese','llamas','sheep'])
    dateinput = DateField("Date In")
    submit = SubmitField("Submit")