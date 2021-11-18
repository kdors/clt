from flask import Blueprint, render_template, request, url_for
import json
import os
import random

bp = Blueprint("clt_main", __name__, url_prefix="/")


@bp.route("/", methods=("GET","POST"))
def index():
   
    data = {}

    if request.method == "POST":
        num_draws = request.form["draws"]
        num_trials = request.form["trials"]

        # get sum data from drawing from a given range at random with replacement a given amount of times 
        # repeated for a given amount of trials
        for i in range(int(num_trials)):
            sum_draws = 0
            for j in range(int(num_draws)):
                draw = random.randint(1, 6)
                sum_draws += draw

            # get a count for number of occurrences of a particular sum
            if sum_draws in list(data):
                data[sum_draws] = data[sum_draws] + 1
            else:
                data[sum_draws] = 1
        
        # convert dictionary keys and values to two lists to convert to JSON 
        # first sort by key value since to visualize data in ascending order by sum number
        sorted_count_data = []
        for key in sorted(data):
            sorted_count_data.append(data[key])

        data_to_json = {}
        data_to_json["sum"] = list(sorted(data))
        data_to_json["count"] = sorted_count_data

        # convert to JSON and write to a file
        with open(os.path.join("clt/static/data.json"),"w") as outfile:
            json.dump(data_to_json, outfile)
        
        return render_template("clt_main/index.html", draws=num_draws, trials=num_trials)

    num_draws = "Not Given"
    num_trials = "Not Given"

    return render_template("clt_main/index.html", draws=num_draws, trials=num_trials)
