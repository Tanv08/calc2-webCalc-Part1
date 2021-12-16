"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.Pylint_controller import PylintController
from app.controllers.AAA_controller import AAAController
from app.controllers.Article1_controller import Article1Controller
from app.controllers.Article2_controller import Article2Controller

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()


@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()


@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()


@app.route("/Pylint", methods=['GET'])
def pylint_get():
    return PylintController.get()


@app.route("/AAA", methods=['GET'])
def AAA_get():
    return AAAController.get()


@app.route("/Article1", methods=['GET'])
def Article1_get():
    return Article1Controller.get()


@app.route("/Article2", methods=['GET'])
def Article2_get():
    return Article2Controller.get()

