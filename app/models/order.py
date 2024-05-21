from datetime import datetime
from app import db
from .order_item import OrderItem

class Order(db.Model):
    """
    Represents an order within the ecommerce system.

    Attributes:
        id (int): The primary key for the Order.
        customer_id (str): A unique identifier for the customer who placed the order.
        status (str): The current status of the order (e.g., 'pending', 'completed', 'shipped').
        items (SQLAlchemy relationship): A dynamic relationship to OrderItem objects that belong to this order.
        total_price (float): The calculated total price of the order.
        created_at (datetime): The timestamp when the order was created. Automatically set to the current UTC time.
    """
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')
    total_price = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def calculate_total(self):
        """
        Calculates the total price of all items in this order and updates the total_price attribute.

        This method iterates over dynamically loaded items, calculates the sum of their subtotals,
        and commits the updated total_price to the database.
        """
        self.total_price = sum(float(item.subtotal) for item in self.items.all())
        db.session.commit()

    def __repr__(self):
        """
        Provides a string representation of this Order instance, useful for debugging and logging.
        
        Returns:
            str: A string indicating the order ID and its customer ID.
        """
        return f'<Order {self.id} Customer {self.customer_id}>'
