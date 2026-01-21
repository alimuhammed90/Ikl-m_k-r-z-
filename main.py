from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/nedenler")
def nedenler():
    return render_template("nedenler.html")

@app.route("/cozumler")
def cozumler():
    return render_template("cozumler.html")

if __name__ == "__main__":
    app.run(debug=True)
