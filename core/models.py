from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="tours")
    name = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    duration_days = models.PositiveIntegerField()
    base_price_cents = models.PositiveIntegerField()
    currency = models.CharField(max_length=10, default="usd")
    includes = models.TextField(blank=True)
    highlights = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Departure(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="departures")
    date = models.DateField()
    capacity = models.PositiveIntegerField()
    available = models.PositiveIntegerField()
    price_cents = models.PositiveIntegerField()
    currency = models.CharField(max_length=10, default="usd")

    class Meta:
        unique_together = ("tour", "date")

    def __str__(self):
        return f"{self.tour.name} - {self.date}"
