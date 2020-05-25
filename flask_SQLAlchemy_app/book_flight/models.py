from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer,primary_key=True)
    origin = db.Column(db.String,nullable=False)
    dest = db.Column(db.String,nullable=False)
    dur = db.Column(db.Integer,nullable=False)

class Passanger(db.Model):
    __tablename__ = "passangers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
