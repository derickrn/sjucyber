from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "sjucyber_secret_key_to_sign_cookies"

# DECLARE USERS HERE
users = {"sjucyber": ("sjucyber", "password123")}


'''DECLARE APP ROUTES'''

# HOME
@app.route("/")
def home():
    return render_template("home.html", name=session.get("username", "Unknown"))

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username][1] == password:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login_wrong.html")
    
    return render_template("login.html")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username not in users:
            users[username] = (username, password)
            return redirect(url_for("login"))
    
    return render_template("register.html")

# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

''' DONE DECLARING APP ROUTES'''


# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=False, port=8080)