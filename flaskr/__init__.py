from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_moment import Moment

from src.database.database import init_app, db
from src.database.models.user_model import User

from src.routes.user_router import user_bp


def create_app(text_config=None):
    app = Flask(__name__)
    Moment(app)
    init_app(app, db)
    Migrate(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )

        response.headers.add(
            "Access-Control-Allow-Methods", "GET,POST,DELETE"
        )

        response.headers.add(
            'Access-Control-Allow-Origin', '*'
        )

        response.headers.add(
            'Access-Control-Allow-Credentials', 'true'
        )

        return response

    @app.route("/", methods=['GET'])
    def get_root_route():
        return (jsonify({
            'success': True,
            'message': "parent route reached. Make a request to /api/v0"
        }), 200)

    @app.route("/api/v0/", methods=["GET"])
    def get_parent_api_route():
        return (jsonify({
            'success': True,
            'message': "Root API route reached"
        }), 201)

    # blueprints
    app.register_blueprint(user_bp, url_prefix="/api/v0/users")

    # catch all routes not defined in API
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return (jsonify({
            "success": False,
            "message": f"The route '{path}' is not defined."
        }), 400)

    return app
