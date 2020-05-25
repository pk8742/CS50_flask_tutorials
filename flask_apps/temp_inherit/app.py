from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    msg = "This is the index page.You can find information here."
    return render_template("index.html",msg=msg)

@app.route("/more")
def more():
    msg = "This is the more page.You can find more information here."
    return render_template("more.html",msg=msg)

if __name__ == '__main__':
    app.run(debug=True)
