from flask import Flask, jsonify, request
#from flask_restful import Resource
import json
import os


app = Flask(__name__)


@app.route("/reservationService/location")
def get_location():
    return "location"


#@app.route("/store", methods=['POST'])


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)