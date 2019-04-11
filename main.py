from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBuG'] = True

@app.route("/signup", methods=['POST'])
def signup():

    name = request.form['name']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    nameError = ""
    passwordError = ""
    verify_passwordError = ""
    emailError = ""

    if (not name) or (name.strip() == ""):
        nameError = "You must enter a name"
    elif (len(name) < 3) or (len(name) > 20) or (" " in name):
        nameError = "Your name must contain 3-20 characters and no spaces"
    
    if (not password) or (password.strip() == ""):
        passwordError = "You must enter a password"
    elif (len(password) < 3) or (len(password) > 20) or (" " in password):
        passwordError = "Your password must contain 3-20 characters and no spaces"
    
    if verify_password != password:
        verify_passwordError = "The passwords you entered do not match. Please try again"

    if not email:
        emailError = ""
    else:
        hasAt = False
        countAt = 0
        hasPeriod = False
        countPeriod = 0

        for char in email:
            if char == "@":
                hasAt = True
                countAt += 1
            elif char == ".":
                hasPeriod = True
                countPeriod += 1

        if (not hasAt) or (countAt > 1) or (not hasPeriod) or (countPeriod > 1) or (len(email) < 3) or (len(email) > 20) or (" " in email):
            emailError = "Not a valid email"

    
    if nameError or passwordError or verify_passwordError or emailError:
        return render_template("home_page.html", name=name, nameError=nameError, password="", passwordError=passwordError, verify_password="", verify_passwordError=verify_passwordError, email=email, emailError=emailError)

    else:
        return redirect('/welcome?name={0}'.format(name))

@app.route("/welcome")
def valid_signup():
    name = request.args.get('name')
    return render_template("welcome_page.html", name=name)

@app.route("/signup", methods=['GET'])
def home_page():
    return render_template('home_page.html')    



@app.route("/")
def index():
    return render_template('home_page.html')


app.run()