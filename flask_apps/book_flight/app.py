from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://postgres:pk8742@localhost:5432/airline')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    """Book a flight"""
    # get more info
    name = request.form.get("name")
    try:
        flight_id = request.form.get("flight_id")
    except ValueError:
        return render_template("error.html",msg="Invalid flight number")
    # make sure flight exists
    if db.execute("SELECT * FROM flights WHERE id = :id",{"id": flight_id}).rowcount == 0:
        return render_template("error.html",msg="no such flight with that id")
    else:
        db.execute("INSERT INTO passangers(name,flight_id) VALUES(:name,:flight_id)",{'name': name,"flight_id": flight_id})
        db.commit() # As far as seeing the results of your insert query, commit your transaction to persist the changes: db.commit()
        return render_template("success.html")

@app.route("/flights")
def flights():
    """Flights List: """
    flights = db.execute("SELECT * FROM flights ORDER BY id ASC").fetchall()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")
def flight_info(flight_id):
    flight = db.execute("SELECT * FROM flights WHERE id = :id",{"id": flight_id}).fetchone()
    # make sure flight exists
    if flight is None:
        return render_template("error.html",msg="No such flight with that id")

    # list passangers
    passangers = db.execute("SELECT name FROM passangers WHERE flight_id = :flight_id",{"flight_id": flight_id}).fetchall()
    return render_template("flight_info.html",flight=flight,passangers=passangers)

db.commit()

if __name__ == '__main__':
    app.run(debug=True)
