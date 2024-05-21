from flask import Blueprint
from app.controllers.order_controller import create_order, get_orders

# Create a Flask Blueprint for order-related routes.
# This blueprint helps to organize code related to order operations, making it reusable and modular.
order_blueprint = Blueprint('order', __name__)

# Define a route for creating orders.
# This route listens to POST requests at /orders and uses the create_order function from the order_controller.
order_blueprint.route('/orders', methods=['POST'])(create_order)

# Define a route for retrieving orders.
# This route listens to GET requests at /orders and uses the get_orders function from the order_controller.
order_blueprint.route('/orders', methods=['GET'])(get_orders)

