import csv

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:pk8742@localhost:5432/airline2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin,dest,dur in reader:
        flight = Flight(origin=origin,dest=dest,dur=dur)
        db.session.add(flight)
        print(f"flight added from {origin} to {dest}, lasting {dur}")
        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        main()
