from flask import Flask


def create_application():
    app = Flask(__name__)

    from .venues import venues
    from .events import events
    from .orders import orders

    app.register_blueprint(venues, url_prefix="/venues")
    app.register_blueprint(events, url_prefix="/events")
    app.register_blueprint(orders, url_prefix="/orders")

    return app
