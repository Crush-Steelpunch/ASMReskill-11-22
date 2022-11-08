# This is Integration testing with Selenium driver

from flask_testing import LiveServerTestCase
from application import app, db
from application.models import Subjects, Staff
from selenium import webdriver


class TestBase(LiveServerTestCase):
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

class TestPage(TestBase):
    def test_case_load_page(self):
        self.driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
        self.driver.get(f'http://localhost:5000.')
        breakpoint()