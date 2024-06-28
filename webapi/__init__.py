from flask import Flask


def create_application():
    app = Flask(__name__)

    from .venues import venues
    from .events import events

    app.register_blueprint(venues, url_prefix="/venues")
    app.register_blueprint(events, url_prefix="/events")

    return app
