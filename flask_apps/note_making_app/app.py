from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/",methods=['POST', 'GET'])
def index():
    session["notes"] = ['']
    if session.get("notes") is None:
        return session["notes"]
    else:
        if request.method == 'POST': # if none of the if / elif clauses are met, then it will return None.
            note = request.form.get("note") # TypeError: The view function did not return a valid response.
            session["notes"].append(note) # The function either returned None or ended without a return statement.
            return render_template("index.html",notes=session["notes"])

if __name__ == '__main__':
    app.run(debug=True)
