from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chi-siamo")
def chi_siamo():
    return render_template("chi_siamo.html")

@app.route("/cucina")
def cucina():
    return render_template("cucina.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/contatti")
def contatti():
    return render_template("contatti.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)