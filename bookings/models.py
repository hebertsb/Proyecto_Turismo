from django.db import models
from django.conf import settings
from core.models import Tour, Departure

class Booking(models.Model):
    Estado = (
        ("pending","PENDIENTE_PAGO"),
        ("paid","PAGADA"),
        ("confirmed","CONFIRMADA"),
        ("completed","REALIZADA"),
        ("canceled","CANCELADA"),
        ("refunded","REEMBOLSADA"),
    )
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT)
    departure = models.ForeignKey(Departure, on_delete=models.PROTECT)
    people = models.PositiveIntegerField(default=1)
    amount_cents = models.PositiveIntegerField()
    currency = models.CharField(max_length=10, default="usd")
    checkout_session_id = models.CharField(max_length=200, blank=True, null=True)
    payment_intent_id = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva #{self.id} - {self.tour.name}"
