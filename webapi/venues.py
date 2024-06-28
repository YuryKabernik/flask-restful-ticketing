from flask import Blueprint


venues = Blueprint('venues', __name__)


@venues.route('')
def get_venues():
    return []


@venues.route('<venue_id>/sections')
def get_venues_sections(venue_id):
    return [venue_id]
