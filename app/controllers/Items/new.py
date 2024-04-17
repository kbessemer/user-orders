from . import blueprint
from flask import request, jsonify
from ...services.items import new

@blueprint.route('/new', methods=['POST'])
def items_new():
    body = request.get_json()

    product_name = body["product_name"]
    product_price = body["product_price"]

    new_item = new(product_name, product_price)

    if new_item:
        return jsonify({
            "success": True,
            "message": "Item added successfully",
            "item": {
                "id": new_item.id,
                "product_name": new_item.product_name,
                "product_price": new_item.price
            }
        }), 201
    else:
        return jsonify({
            "success": False,
            "message": "Failed to add the item"
        }), 500
