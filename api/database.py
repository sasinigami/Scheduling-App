from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# create database
meeting = db.Table('meeting',
    db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
    db.Column('appointment_id', db.Integer, db.ForeignKey('appointment.id'))
)

class Person(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80), unique=False, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    meetings = db.relationship('Appointment', secondary=meeting, backref=db.backref('meets', lazy='dynamic'))

    def __repr__(self) -> str:
        return 'User>>> {self.name}'

# create person schema
class PersonSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email')

person_schema = PersonSchema(many=False)
persons_schema = PersonSchema(many=True)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80), unique=False, nullable=False)
    content=db.Column(db.String(80), unique=False, nullable=False)
    start = db.Column(db.DateTime(), nullable=False)
    end = db.Column(db.DateTime(), nullable=False)
