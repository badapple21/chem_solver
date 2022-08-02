from crypt import methods
import os
from flask import Flask, redirect, render_template, request, session, json
from flask_session import Session
from solver import solve, format

# configure application
app = Flask(__name__)

# Ensure auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fetch")
def fetch():
    q = request.args.get("q")
    w = request.args.get("w")
    e = request.args.get("e")
    r = request.args.get("r")
    t = request.args.get("t")
    y = request.args.get("y")

    if q and w and e and r and t and y:
        status, coefficient1, coefficient2, charge1, charge2, reactant1, reactant2, t, y, product_coefficient = solve(
            q, w, e, r, t, y)
        if(status == "Error"):
            rtnHTML = "Could not calculate"
        else:
            rtnHTML = format(coefficient1, coefficient2, int(charge1),
                             int(charge2), reactant1, reactant2, int(t), int(y), int(product_coefficient))

    else:
        rtnHTML = "Error - enter all felids"

    return rtnHTML

@app.route("/periodic_table")
def periodic_table():
    return render_template("periodic_table.html")

@app.route("/polyatomic_ions")
def polyatmoic_ions():
    return render_template("polyatomic_ions.html")
