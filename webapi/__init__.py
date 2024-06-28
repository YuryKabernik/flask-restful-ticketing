from flask import Flask


def create_application():
    app = Flask(__name__)

    from .venues import venues

    app.register_blueprint(venues, url_prefix='/venues')
    
    return app
