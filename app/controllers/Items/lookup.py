from . import blueprint
from flask import request, jsonify
from ...services.items import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def items_lookup(id):
    body = request.get_json()

    page = body["page"]
    page_size = body["page_size"]

    query = lookup(id, page, page_size)

    review_data = []

    if query["item"]:
        for review in query["item"].reviews:
                    data = {
                        "comment": review.comment
                    }
                    review_data.append(data)

        return jsonify({
            "success": True,
            "message": "Item found",
            "item": {
                "id": query["item"].id,
                "product_name": query["item"].product_name,
                "product_price": query["item"].price,
                "reviews": review_data
            },
            "pagination": query["pagination"]
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the item"
        }), 404
