from flask import Blueprint


events = Blueprint('events', __name__)


@events.route('')
def get_events():
    return {'events': []}


@events.route('<event_id>/sections/<section_id>/seats')
def get_event_seates(event_id, section_id):
    return {'event': event_id, 'sections': section_id, "seats": []}
