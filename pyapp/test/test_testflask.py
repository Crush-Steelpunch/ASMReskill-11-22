from flask_testing import TestCase
from application import app, db
from application.models import Subjects, Staff
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app

    def setUp(self):
        db.create_all()
        for subj in ['Jankins','Pythud','Flop']:
            subjects = Subjects(subject_name=subj)
            db.session.add(subjects)
        data1 = {'Melon':2,'Derp':1,'Madman':2,'Barry':3}
        for nme in data1:
            staff = Staff(staff_name=nme,subject_id=data1[nme])
            db.session.add(staff)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

class TestReadDB(TestBase):
    
    def test_dbSubread(self):
        var1 = Subjects.query.first()
        assert var1.subject_name == 'Jankins'
    def test_dbStaffread(self):
        var2 = Staff.query.first()
        assert var2.staff_name == 'Melon'
    def test_query_all_staff(self):
        var1 = Staff.query.all()
        namesvar = []
        for i in var1:
            namesvar.append(i.staff_name)
        assert 'Madman' in namesvar


class TestReadURL(TestBase):

    def test_200OK(self):
        responsevar = self.client.get(url_for('read'))
        assert responsevar.status_code == 200
    def test_Fabulous(self):
        responsevar = self.client.get(url_for('read'))
        assert "Madman" in responsevar.text 