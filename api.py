# importing nse from nse tools
from nsetools import Nse

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# creating a Nse object
nse = Nse()


@app.route("/", methods=["GET"])
def home():
    return """<h1>Home Page</h1>"""


@app.route("/allcodes", methods=["GET"])
def all_codes():
    return jsonify(nse.get_stock_codes())


@app.route("/stocks", methods=["GET"])
def api_stocks():
    return jsonify(nse.get_quote(request.args.get('id')))


@app.route("/advancedecline", methods=["GET"])
def advance_decline():
    return jsonify(nse.get_advances_declines())

@app.route("/indexlist", methods=["GET"])
def index_list():
    return jsonify(nse.get_index_list())


@app.route("/topgain", methods=["GET"])
def top_gainers():
    return jsonify(nse.get_top_gainers())


@app.route("/indexquote", methods=["GET"])
def index_quote():
    return jsonify(nse.get_index_quote(request.args.get('id')))


app.run()
