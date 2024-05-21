from datetime import datetime
from app import db

class OrderItem(db.Model):
    """
    Represents an item within an order in the database.

    Attributes:
        id (int): The primary key for the OrderItem.
        order_id (int): Foreign key reference to the Order this item belongs to.
        product_id (int): The identifier for the product this item represents.
        quantity (int): The number of units of the product in this order item.
        price_per_unit (float): The price per unit of the product at the time the order was placed.
        created_at (datetime): The timestamp when the order item was created, automatically set to the current time.
    """

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def subtotal(self):
        """
        Calculate and return the subtotal for this order item.
        
        Returns:
            float: The subtotal, which is the product of quantity and price per unit.
        """
        return self.quantity * self.price_per_unit

    def __repr__(self):
        """
        Provide a string representation of the OrderItem instance, which is helpful for debugging.

        Returns:
            str: A string representation of the OrderItem instance.
        """
        return f'<OrderItem {self.id} for Order {self.order_id}>'
