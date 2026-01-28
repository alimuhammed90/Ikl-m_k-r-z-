from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/nedenler")
def nedenler():
    return render_template("nedenler.html")

@app.route("/cozumler")
def cozumler():
    return render_template("cozumler.html")

@app.route("/neden_yapmamaliyiz")
def neden_yapmamalıyiz():
    return render_template("neden_yapmamaliyiz.html")

@app.route("/tesvik")
def tesvik():
    return render_template("tesvik.html")


if __name__ == "__main__":
    app.run(debug=True)
