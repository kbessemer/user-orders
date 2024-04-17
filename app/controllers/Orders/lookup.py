from . import blueprint
from flask import jsonify
from ...services.orders import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def orders_lookup(id):
    order = lookup(id)

    if order:
        items_list = [{
            "product_name": order_item.item.product_name,
            "product_price": order_item.item.price,
            "quantity": order_item.quantity,
        } for order_item in order.items]

        return jsonify({
            "success": True,
            "message": "Order found",
            "order": {
                "id": order.id,
                "order_date": order.order_date,
                "items": items_list
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the order"
        }), 404