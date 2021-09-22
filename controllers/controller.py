from app import app
from flask import render_template
from models.order_list import orders


@app.route('/')
def index():
    return "Hello, peeps"

@app.route('/orders')
def order():
    return render_template("index.html", title="this", orders = orders)