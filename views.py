from flask import Blueprint, render_template, request, redirect, session

views = Blueprint('views', __name__)

# ================= index.html homepage ================= 

@views.route('/')
def home():
    return render_template("index.html")

# ================= login.html login page ================= 

@views.route("/login")
def login_page():
    return render_template("login.html")

# ================= login.html login form ================= 

maxtries = 3

@views.route("/login", methods=["POST"])
def login():
    if "tries" not in session:
        session["tries"] = 0

    if session["tries"] >= maxtries:
        return "Locked out."
    
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "password":
        session["user"] = username # part of session authentication
        session["tries"] = 0 
        return redirect("/login/welcome")
    else:
        session["tries"] += 1
        newtries = maxtries - session["tries"]

        if session["tries"] >= maxtries:
            return "Locked out. Please close and reopen the browser to try again."
        
        return "Incorrect password. Tries remaining: " + str(newtries)
        

# ================= welcome.html welcome page ================= 

@views.route("/login/welcome")
def login_welcome():
    if "user" not in session: # part of session authentication
        return redirect("/login")
    return render_template("welcome.html")