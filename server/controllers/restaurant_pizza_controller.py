from flask import jsonify, request
from server.app import app, db  
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        restaurant = Restaurant.query.get(data['restaurant_id'])
        pizza = Pizza.query.get(data['pizza_id'])
        if not restaurant or not pizza:
            return jsonify({"errors": ["Restaurant or Pizza not found"]}), 404
        
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            restaurant_id=data['restaurant_id'],
            pizza_id=data['pizza_id']
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400