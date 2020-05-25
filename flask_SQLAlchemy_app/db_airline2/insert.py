from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:pk8742@localhost:5432/airline2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    new_flight = flight(origin="New York",dest="Paris",dur=540)
    db.session.add(new_flight)

if __name__ == '__main__':
    with app.app_context():
        main()
