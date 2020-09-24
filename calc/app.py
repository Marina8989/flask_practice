# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route("/add")
def add_num():
    """Add a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def sub_num():
     """Subtract a and b"""

     a = int(request.args.get("a"))
     b = int(request.args.get("b"))
     result = sub(a, b)

     return str(result)  

