from flask import Flask
from authomatic import Authomatic
from flask.ext.pymongo import PyMongo

from settings import CONFIG

app = Flask(__name__)
authomatic = Authomatic(
    CONFIG, 'fnsjknf897jcnsd$%#DSFDCskc9', report_errors=False)
mongo = PyMongo(app)


if __name__ == '__main__':
    from routers import *
    app.secret_key = "njnf334#@mkedk4534#!@cmks^^&_"
    app.run(debug=True, port=8000, host="0.0.0.0")