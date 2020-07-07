from flask import Flask, jsonify, request, redirect, url_for, abort
from flask_restful import Resource


app = Flask(__name__)


@app.route('/homepage')
def homepage():
	return "Hello World"

@app.route('/test/<param>')
def test(param):
	toReturn = "Your passed in parameter was '" + param + "'"
	return toReturn

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=3000)