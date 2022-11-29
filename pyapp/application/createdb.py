from application import db
from application.models import Subjects,Staff

def populate():
    
    db.create_all()
    
    for subj in ['Jenkins','Python','Flask']:
        subjects = Subjects(subject_name=subj)
        db.session.add(subjects)
    db.session.commit()
    data1 = {'Leon':2,'Earl':1,'Adam':2,'Harry':3}
    for nme in data1:
        staff = Staff(staff_name=nme,subject_id=data1[nme])
        db.session.add(staff)
    db.session.commit()
