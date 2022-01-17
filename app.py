import os
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Mail, Message


from helpers import apology, login_required

# Configure application
app = Flask(__name__)
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 465
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
mail = Mail(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use Postgresql Heroku database
uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://")
db = SQL(uri)

""" Moving to database
# Breakfast menu
MENU = [
    "Potato Bagel",
    "Creame Cheese Bagel",
    "Tuna Bagel",
    "Egg Salad Bagel",
    "Breakfast Special"
]
"""

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Allow user to make a breakfast selection"""
    # Bagel shop selection menu
    # get user current selection
    #TODO
    [pastSelection] = db.execute("SELECT sun, mon, tue, wed, thu FROM users WHERE id = (?)", session["user_id"])
    # Get Breakfast Choice
    #TODO
    menu = db.execute("SELECT * FROM menu") 

    return render_template("index.html", selection=pastSelection, menu=menu)


@app.route("/selection", methods=["POST"])
@login_required
def selection():

    # User submitted breakfast selection 
    selection = {}
    for day in ['sun', 'mon', 'tue', 'wed', 'thu']:
        selection[day] = request.form.get("day")
    print(selection)

    # Validate users selection
    #if selection not in MENU:
        #return apology("Invalid breakfast choice", 400)
    
    # Add selection to db
    #db.execute("UPDATE users SET breakfast = (?) WHERE id = (?)",
     #           selection, session["user_id"])
    #message = Message("test worked!", recipients=["app@habet.dev"])
    #mail.send(message)
    return render_template("success.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Check if username exists
        elif len(db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))):
            return apology("Sorry, username already taken", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmed
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password mismatch", 400)

        # Insert username into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"),
                   generate_password_hash(request.form.get("password")))


        # Query database for username
        rows = db.execute("SELECT id FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


