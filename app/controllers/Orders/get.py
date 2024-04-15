from . import orders
from flask import jsonify
from ...services.Orders import get

@orders.route('/lookup/<int:id>', methods=['GET'])
def orders_get(id):
    order = get(id)

    if order:
        items_list = [{
            "product_name": item.product_name,
            "product_price": item.price
        } for item in order.items]

        return jsonify({
            "success": True,
            "message": "Order found",
            "order": {
                "id": order.id,
                "items": items_list
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the order"
        }), 404
