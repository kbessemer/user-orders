from . import blueprint
from flask import request, jsonify
from ...services.items import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def items_lookup(id):
    item = lookup(id)

    review_data = []

    for review in item.reviews:
                    data = {
                        "comment": review.comment
                    }
                    review_data.append(data)

    if item:
        return jsonify({
            "success": True,
            "message": "Item found",
            "item": {
                "id": item.id,
                "product_name": item.product_name,
                "product_price": item.price,
                "reviews": review_data
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the item"
        }), 404
