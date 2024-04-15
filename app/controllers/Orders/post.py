from . import orders
from ...services.Users import get
from ...services.Orders import post
from ...models.order import Order

@orders.route('/new', methods=['POST'])
def orders_post():
    from flask import request, jsonify
    data = request.get_json()

    user_id = data['user_id']
    item_ids = data['item_ids']

    user = get(user_id)
    if not user:
        return jsonify({
            "success": False,
            "message": "Failed to find the user"
        }), 404

    order = post(user, item_ids)

    if order:
        return jsonify({
            "success": True,
            "message": "Order added successfully",
            "order": {
                "id": order.id
            }
        }), 201
    else:
        return jsonify({
            "success": False,
            "message": "Failed to add the order"
        }), 500