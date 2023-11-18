from flask import Blueprint, jsonify

user_bp = Blueprint("user_blueprint", __name__)


@user_bp.route("/")
def get_user():
    return jsonify({"status": 'success',
                    "data": {
                        "data": {"name": "louis"}
                    }})
