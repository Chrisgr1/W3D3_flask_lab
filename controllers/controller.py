from flask import render_template
from app import app
from models.order_list import orders

@app.route('orders)')
def index():
    return render_template('index.html', title ='Chris Cool Stuff', orders=orders)

@app.route('orders/<index>')
def get_one_order(index):
    order = orders(int(index))
    return render_template()