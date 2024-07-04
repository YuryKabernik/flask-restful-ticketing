from flask import Blueprint


orders = Blueprint("orders", __name__)


@orders.route("cart/<cart_id>")
def get_cart_items(cart_id):
    return []


@orders.route("carts/<cart_id>", methods=["POST"])
def add_cart_item(cart_id):
    return {"cartId": cart_id}


@orders.route("carts/<cart_id>/events/<event_id>/seats/<seat_id>", methods=["DELETE"])
def remove_seat_from_cart(cart_id, event_id, seat_id):
    return {"cartId": cart_id, "eventId": event_id, "seatId": seat_id}


@orders.route("carts/<cart_id>/book", methods=["PUT"])
def book_cart_items(cart_id):
    return {"paymentId": f"{cart_id}-payment-guid"}
