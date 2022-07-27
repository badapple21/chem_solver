import os
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

#configure application
app = Flask(__name__)

#Ensure auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")


