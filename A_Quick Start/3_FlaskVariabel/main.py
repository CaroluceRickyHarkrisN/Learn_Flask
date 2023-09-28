# First we import flask
from flask import Flask

# initialize flask
app = Flask(__name__)

# Display first simple welcome msg
@app.route('/')
def msg():
	return "Welcome"

# We defined string function
@app.route('/vstring/<name>')
def string(name):
	return "My Name is %s" % name

# define int function
@app.route('/vint/<int:age>')
def vint(age):
    return "I am %d years old " % age

# define float function
@app.route('/vfloat/<float:balance>')
def vfloat(balance):
    return "My Account Balance %f" % balance

# we run app debugging mode
app.run(debug=True)
