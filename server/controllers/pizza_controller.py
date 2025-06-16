from flask import jsonify
from server.app import app  
from server.models.pizza import Pizza

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])