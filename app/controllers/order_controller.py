from flask import jsonify, request
from app import db
from app.models.order import Order
from app.models.order_item import OrderItem

def create_order():
    """
    Create a new order with items from a JSON request.

    Processes a JSON payload to create an order and its associated items, computes total,
    and commits the transaction to the database.

    Returns:
        Response: JSON object with the message and created order ID, status code 201.
    """
    data = request.get_json()
    
    try:
        # Create a new order instance
        order = Order(customer_id=data['customer_id'], status='completed')
        db.session.add(order)
        db.session.flush()  # Flush to get the order ID for the order_items

        # Create order items from the provided item data
        for item_data in data['items']:
            item = OrderItem(
                order_id=order.id,
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                price_per_unit=item_data['price_per_unit']
            )
            db.session.add(item)

        # Calculate the total price for the order
        order.calculate_total()
        db.session.commit()
        
        return jsonify({'message': 'Order created', 'order_id': order.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

def get_orders():
    """
    Retrieve all orders from the database.

    Returns:
        Response: JSON list of all orders with their details and associated items.
    """
    orders = Order.query.all()
    orders_data = [{
        'id': order.id,
        'customer_id': order.customer_id,
        'status': order.status,
        'total_price': order.total_price,
        'created_at' : order.created_at.isoformat(),
        'items': [{
            'product_id': item.product_id, 
            'quantity': item.quantity, 
            'price_per_unit': item.price_per_unit
        } for item in order.items.all()]
    } for order in orders]

    return jsonify(orders=orders_data)
