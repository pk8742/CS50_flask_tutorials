from flask import Flask, render_template,request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:pk8742@localhost:5432/airline2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.dest} lasting {flight.dur}")

if __name__ == '__main__':
    with app.app_context():
        main()
