from . import blueprint
from flask import request, jsonify
from ...services.users import new

@blueprint.route('/new', methods=['POST'])
def users_new():
    body = request.get_json()

    first_name = body["first_name"]
    last_name = body["last_name"]

    new_user = new(first_name, last_name)

    if new_user:
        return jsonify({
            "success": True,
            "message": "User added successfully",
            "user": {
                "id": new_user.id,
                "first_name": new_user.first_name,
                "last_name": new_user.last_name
            }
        }), 201
    else:
        return jsonify({
            "success": False,
            "message": "Failed to add the user"
        }), 500
