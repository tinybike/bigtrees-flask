#!/usr/bin/env python
"""
bigtrees web app

"""
from __future__ import division
import os
from flask import Flask, request, render_template

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
app.debug = "DYNO" not in os.environ
app.config["datafile"] = os.path.join("app", "data", "TP001_jenkins.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    # get species and quantity from the form
    species = request.form["species"]
    quantity = round(float(request.form["quantity"]), 1)

    # open the csv data file and go through it line by line until we find
    # a line that matches both the requested species and quantity
    with open(app.config["datafile"]) as datafile:
        for line in datafile:
            splitline = line.strip().split(',')

            # check if species matches the requested species
            species_from_file = splitline[0].strip('"')
            if species == species_from_file:

                # check if the quantity matches the requested quantity
                quantity_from_file = float(splitline[1])
                if quantity == quantity_from_file:

                    # this is the value we want!
                    # send it back to the template (index.html) so the user
                    # can see it
                    return render_template("index.html", lookup=splitline[2])

    # if we've reached this point, then we didn't find a match.
    # send an error message to the template (index.html) so the user knows
    # the lookup wasn't successful
    return render_template("index.html", lookup="No match found")

def main():
    if app.debug:
        app.run(port=port)
    else:
        app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
