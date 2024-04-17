from . import blueprint
from ...services.users import lookup
from ...services.orders import new

@blueprint.route('/new', methods=['POST'])
def orders_new():
    from flask import request, jsonify
    data = request.get_json()

    user_id = data['user_id']
    item_data = data['item_data']

    user = lookup(user_id)
    if not user:
        return jsonify({
            "success": False,
            "message": "Failed to find the user"
        }), 404

    order = new(user, item_data)

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