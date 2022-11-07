from application import db
from application.models import Subjects,Staff

#create db
db.drop_all()
db.create_all()
# populate DB

for subj in ['Jenkins','Python','Flask']:
    subjects = Subjects(subject_name=subj)
    db.session.add(subjects)
db.session.commit()
data1 = {'Leon':2,'Earl':1,'Adam':2,'Harry':3}
for nme in data1:
    staff = Staff(staff_name=nme,subject_id=data1[nme])
    db.session.add(staff)
db.session.commit()

# print some stuff from the db
for i in db.session.query(Subjects):
    print(i.id, i.subject_name)

for row in db.session.query(Staff).join(Subjects).all():
    print(row.staff_name,row.subject_idbr.subject_name)