from flask import Blueprint


payments = Blueprint("payments", __name__)


@payments.route("<payment_id>")
def get_payment(payment_id):
    return {"paymentId": payment_id}


@payments.route("<payment_id>/complete")
def complete_payment(payment_id):
    return {"paymentId": payment_id}


@payments.route("<payment_id>/failed")
def fiail_payment(payment_id):
    return {"paymentId": payment_id}
