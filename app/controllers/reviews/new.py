from . import blueprint
from ...services.reviews import new
from ...services.items import lookup
from flask import request, jsonify

@blueprint.route('/new', methods=['POST'])
def orders_new():
    data = request.get_json()

    item_id = data['item_id']

    item = lookup(item_id)
    if not item:
        return jsonify({
            "success": False,
            "message": "Failed to find the item"
        }), 404

    review = new(item, data)

    if review:
        return jsonify({
            "success": True,
            "message": "Review added successfully",
            "order": {
                "id": review.id
            }
        }), 201
    else:
        return jsonify({
            "success": False,
            "message": "Failed to add the review"
        }), 500