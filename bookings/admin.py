from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import Booking

# Traducción de estados
ESTADOS_ES = {
    "pending":   "Pendiente de pago",
    "paid":      "Pagada",
    "confirmed": "Confirmada",
    "completed": "Realizada",
    "canceled":  "Cancelada",
    "refunded":  "Reembolsada",
}

# Filtro personalizado por estado (en español)
class EstadoListFilter(SimpleListFilter):
    title = "Estado"
    parameter_name = "estado"

    def lookups(self, request, model_admin):
        return [(v, k) for k, v in ESTADOS_ES.items()]  # Mostrar estado en español

    def queryset(self, request, queryset):
        # Obtener el valor de estado traducido
        if self.value():
            # Encontrar la clave en inglés a partir del estado en español
            inv = {v: k for k, v in ESTADOS_ES.items()}
            estado_db = inv.get(self.value())
            if estado_db:
                return queryset.filter(status=estado_db)  # Filtrar por el valor en la BD
        return queryset

@admin.register(Booking)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "mostrar_tour",
        "mostrar_salida",
        "mostrar_usuario",
        "mostrar_personas",
        "mostrar_importe",
        "mostrar_moneda",
        "mostrar_estado",
        "mostrar_creado",
    )
    list_select_related = ("tour", "departure", "user")
    list_filter = (EstadoListFilter, "currency", "created_at", "tour")  # Usamos el filtro en español
    search_fields = ("tour__name", "user__username", "id", "departure__id")
    ordering = ("-created_at",)

    # --- Columnas traducidas ---
    def mostrar_tour(self, obj):
        return getattr(obj.tour, "name", f"Tour #{obj.tour_id}")
    mostrar_tour.short_description = "Tour"

    def mostrar_salida(self, obj):
        nombre = getattr(obj.departure, "name", None)
        if nombre:
            return nombre
        fecha = getattr(obj.departure, "date", None)
        return fecha or f"Salida #{obj.departure_id}"
    mostrar_salida.short_description = "Salida"

    def mostrar_usuario(self, obj):
        return getattr(obj.user, "username", obj.user_id)
    mostrar_usuario.short_description = "Usuario"

    def mostrar_personas(self, obj):
        return obj.people
    mostrar_personas.short_description = "Personas"

    def mostrar_importe(self, obj):
        try:
            return f"{obj.amount_cents/100:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except Exception:
            return obj.amount_cents
    mostrar_importe.short_description = "Importe"

    def mostrar_moneda(self, obj):
        return (obj.currency or "").upper()
    mostrar_moneda.short_description = "Moneda"

    def mostrar_estado(self, obj):
        return ESTADOS_ES.get(obj.status, obj.status)
    mostrar_estado.short_description = "Estado"

    def mostrar_creado(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M")
    mostrar_creado.short_description = "Creado en"
