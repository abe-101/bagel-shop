import os
import datetime
import markdown
import markdown.extensions.fenced_code
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_mail import Mail, Message
from flask_apscheduler import APScheduler
from pygments.formatters import HtmlFormatter
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

# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


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

# interval example
@scheduler.task('cron', id='do_job_1', week='*', day_of_week='thur', hour='9', minute='2')
def job1():
    with scheduler.app.app_context():
        message = Message("test worked!", recipients=["app@habet.dev"])
        mail.send(message)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/about")
def about():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )
    formatter = HtmlFormatter(style="emacs",full=True,cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"
    md_template = md_css_string + md_template_string
    return md_template

@app.route("/")
@login_required
def index():
    """Allow user to make a breakfast selection"""
    # Bagel shop selection menu
    # get user current selection
    [pastSelection] = db.execute("SELECT sunday, monday, tuesday, wednessday, thursday FROM users WHERE id = (?)", session["user_id"])
    # Get menu from db as a list
    menu = [i['item'] for i in db.execute("SELECT item FROM menu")]

    return render_template("index.html", selection=pastSelection, menu=menu)


@app.route("/selection", methods=["POST"])
@login_required
def selection():

    # Get menu from db as a list
    menu = [i['item'] for i in db.execute("SELECT item FROM menu")]
    
    # User submitted breakfast selection
    for day in ['sunday', 'monday', 'tuesday', 'wednessday', 'thursday']:
        choice = request.form.get(day)
        ww = request.form.get(day+"-ww")
        if choice == None:
            continue
        elif choice in menu:
            if ww == 'on':
                choice = "WW-"+choice
            print(choice)
            db.execute(f"UPDATE users SET {day}=(?) WHERE id = (?)", choice, session["user_id"])
        else:
            return apology("Not a valid selection", 403)

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
        email = request.form.get("username")
        password = request.form.get("password")

        if not email:
            return apology("must provide username", 400)

        # Check if username exists
        elif len(db.execute("SELECT * FROM users WHERE username = ?", email)):
            return apology("Sorry, username already taken", 400)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 400)

        # Ensure password confirmed
        elif password != request.form.get("confirmation"):
            return apology("password mismatch", 400)

        # Insert username into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", email,
                   generate_password_hash(password))

        # Send welcome message
        message = Message("Thank you for registering", recipients=[email])
        mail.send(message)

        # Query database for username
        rows = db.execute("SELECT id FROM users WHERE username = ?", email)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


