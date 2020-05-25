from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:pk8742@localhost:5432/airline2'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # tie this database with this flask application

@app.route("/")
def index():
    flights = Flight.query.order_by(Flight.id.asc()).all()
    return render_template("index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    """Book a flight"""
    # get more info
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",msg="Invalid flight number")
    # make sure flight exists
    flight = Flight.query.get(flight_id)
    if not flight:
        return render_template("error.html",msg="no such flight with that id")
    else:
        flight.add_passanger(name) # add passanger
        return render_template("success.html")

@app.route("/flights")
def flights():
    """Flights List: """
    flights = Flight.query.order_by(Flight.id.asc()).all()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")
def flight_info(flight_id):
    flight = Flight.query.get(flight_id)
    # make sure flight exists
    if flight is None:
        return render_template("error.html",msg="No such flight with that id")

    # list passangers
    passangers = Passanger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight_info.html",flight=flight,passangers=passangers)


if __name__ == '__main__':
    app.run(debug=True)
