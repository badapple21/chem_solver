from crypt import methods
import os
from flask import Flask, redirect, render_template, request, session, json
from flask_session import Session
from solver import solve, format

# configure application
app = Flask(__name__)

# Ensure auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

#render main page
@app.route("/")
def index():
    return render_template("index.html")


#fetch route for looking uop elements on the periodic table page
@app.route("/fetch_lookup_element")
def fetch_lookup_elemetn():
    q = request.args.get("w")
    if q:
        possible_elements = periodic.lookup_element(q)
        HTML = ""
        for possible_element_number in possible_elements:
            e = periodic.Element(possible_element_number)
            HTML += e.lookup()

        print(HTML)
        return HTML


#fetch request for solving the equation
@app.route("/fetch")
def fetch():
    q = request.args.get("q")
    w = request.args.get("w")
    e = request.args.get("e")
    r = request.args.get("r")
    t = request.args.get("t")
    y = request.args.get("y")
    
    #checks if user has enterd all the feilds
    if q and w and e and r and t and y:
        status, coefficient1, coefficient2, charge1, charge2, reactant1, reactant2, t, y, product_coefficient = solve(
            q, w, e, r, t, y)
        # if the solver could not work up a soultion
        if(status == "Error"):
            rtnHTML = "Could not calculate"
        else:
            # formats the data to a string for the html
            rtnHTML = format(coefficient1, coefficient2, int(charge1),
                             int(charge2), reactant1, reactant2, int(t), int(y), int(product_coefficient))

    else:
        rtnHTML = "Error - enter all felids"

    return rtnHTML

# renders periodic table
@app.route("/periodic_table")
def periodic_table():
    return render_template("periodic_table.html")

#renders polyatomic_ions
@app.route("/polyatomic_ions")
def polyatmoic_ions():
    return render_template("polyatomic_ions.html")
