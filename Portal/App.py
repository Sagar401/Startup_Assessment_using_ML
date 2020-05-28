
import os
import numpy as np
import flask
import pickle
from flask import Flask, redirect, render_template
app= Flask(__name__)

@app.route("/")
def Home():
	return render_template("HomePage.html")

@app.route('/HomePage')
def HomePage():
	return render_template("HomePage.html")

@app.route('/Analysis')
def Analysis():
	return render_template("Analysis.html")

@app.route('/Team')
def Team():
	return render_template("Team.html")

@app.route('/MainDashboard')
def MainDashboard():
	return render_template("MainDashboard.html")



if __name__ == "__main__":
	app.run(debug=True)