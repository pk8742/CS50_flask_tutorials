from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more",methods=["POST"])
def more():
    name = request.form.get("name")
    return render_template("more.html",name=name)

if __name__ == '__main__':
    app.run(debug=True)
