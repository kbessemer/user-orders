from . import items
from flask import request, jsonify
from ...services.Items import get

@items.route('/lookup/<int:id>', methods=['GET'])
def items_get(id):
    item = get(id)

    if item:
        return jsonify({
            "success": True,
            "message": "Item found",
            "item": {
                "id": item.id,
                "product_name": item.product_name,
                "product_price": item.price
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the item"
        }), 404
