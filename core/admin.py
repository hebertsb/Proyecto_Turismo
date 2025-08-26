from django.contrib import admin
from .models import Tour, Departure

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ("id", "col_nombre", "col_precio", "col_moneda")
    search_fields = ("name", "id")
    ordering = ("id",)

    def col_nombre(self, obj):
        return getattr(obj, "name", f"Tour #{obj.id}")
    col_nombre.short_description = "Nombre"

    def col_precio(self, obj):
        # Asume price_cents; ajusta si tu campo se llama distinto.
        cents = getattr(obj, "price_cents", None)
        if cents is None:
            return "-"
        return f"{cents/100:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    col_precio.short_description = "Precio"

    def col_moneda(self, obj):
        cur = getattr(obj, "currency", "")
        return (cur or "").upper()
    col_moneda.short_description = "Moneda"

@admin.register(Departure)
class DepartureAdmin(admin.ModelAdmin):
    list_display = ("id", "col_tour", "col_fecha")
    list_filter = ("tour", "date")  # ajusta “date” si tu modelo usa otro nombre
    search_fields = ("tour__name", "id")
    ordering = ("-date", "id")

    def col_tour(self, obj):
        return getattr(obj.tour, "name", f"Tour #{obj.tour_id}")
    col_tour.short_description = "Tour"

    def col_fecha(self, obj):
        # Ajusta si tu modelo no usa “date”
        return getattr(obj, "date", "-")
    col_fecha.short_description = "Fecha"
