from celery import shared_task
from payments.models import Payment

@shared_task
def update_booking_status(payment_id):
    try:
        payment = Payment.objects.select_related('booking').get(id=payment_id)
    except Payment.DoesNotExist:
        return f"Payment {payment_id} does not exist"

    booking = payment.booking
    if not booking:
        return f"Payment {payment_id} has no associated booking"

    if payment.status == 'succeeded':
        booking.status = 'confirmed'
        booking.save()
        return f"Booking {booking.id} confirmed"
    return f"Payment {payment_id} status is not succeeded"

