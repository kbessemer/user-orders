from . import blueprint
from flask import request, jsonify
from ...services.users import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def users_lookup(id):
    user = lookup(id)

    if user:
        user_data = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "orders": []
        }

        for order in user.orders:
            order_data = {
                "order_id": order.id,
                "order_date": order.order_date,
                "items": []
            }

            for item in order.items:
                item_data = {
                    "product_name": item.item.product_name,
                    "product_price": item.item.price,
                    "quantity": item.quantity,
                    "reviews": []
                }
                order_data["items"].append(item_data)

            user_data["orders"].append(order_data)

        return jsonify({
            "success": True,
            "message": "User found",
            "user": user_data
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the user"
        }), 404
