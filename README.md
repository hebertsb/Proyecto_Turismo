# Proyecto_Turismo
1. Introducción
El proyecto es una plataforma de software web y móvil para turismo, diseñada para Bolivia. Permite a los usuarios:
- Reservar tours y otros servicios turísticos.
- Pagar online de manera segura.
- Consultar y recibir recomendaciones inteligentes.
- Permite a los operadores y administradores gestionar servicios, reservas y reportes.

Está construido con Django (backend), SQLite (base de datos) y React/Flutter (frontend).

---

2. Estructura General del Proyecto

El proyecto está organizado en varias carpetas y aplicaciones:

2.1 Carpeta 'sitio/':
- Contiene la configuración global de Django.
- Archivos clave:
    - settings.py: Configuración de la base de datos, apps instaladas, middleware, autenticación, etc.
    - urls.py: Rutas principales del proyecto.
    - wsgi.py: Configuración para producción (WSGI server).
    
2.2 Apps principales (cada carpeta representa un módulo funcional):

- accounts/: Gestión de usuarios, roles, permisos y autenticación.
- bookings/: Gestión de reservas, pagos y estados de reservas.
- payments/: Procesamiento de pagos y cupones.
- sales/: Cotizaciones y ventas realizadas por agentes.
- operators/: Gestión de operadores (guías, conductores, proveedores).
- reviews/: Gestión de reseñas de tours o servicios.
- cms/: Sistema de contenido administrativo.
- core/: Contiene entidades centrales como Tour y Departure.

2.3 Carpeta packages/:
- Contiene código reutilizable y casos de uso (use_cases) para organizar la lógica de negocio.
- Subcarpetas típicas:
    - reservas_pagos/: Casos de uso y API de reservas y pagos.
    - ventas_cotizaciones/: Casos de uso y API de cotizaciones.
    - operadores_servicios/: Casos de uso y API para operadores.
    - admin_config/: Configuraciones globales y administración.

---

3. Modelos y Base de Datos

Cada app tiene un archivo models.py que define los modelos:
- Booking: Tabla de reservas (usuario, tour, fecha de salida, cantidad de personas, estado, pago).
- Tour: Tabla de tours (nombre, precio, descripción).
- Departure: Tabla de salidas de cada tour (fecha y detalles).
- User: Tabla de usuarios extendida desde el modelo de Django.

El ORM de Django se encarga de transformar estos modelos en **tablas en la base de datos SQLite**.

---

4. Serializadores (serializers.py)

- Los serializadores transforman datos de los modelos de Django a JSON y viceversa.
- Ejemplo: BookingSerializer convierte objetos Booking para que puedan enviarse/recibirse por la API.

---

5. Vistas y ViewSets (views.py / viewsets.py)

- ViewSets permiten crear endpoints CRUD automáticamente (Crear, Leer, Actualizar, Eliminar).
- Cada módulo tiene su ViewSet:
    - BookingViewSet: Gestiona reservas y aplica permisos (solo usuario dueño o admin puede ver todas).
- Las vistas manejan las solicitudes HTTP (GET, POST, PUT, DELETE).

---

6. Rutas y URLs (urls.py)

- Cada app define sus rutas internas en urls.py.
- En sitio/urls.py se incluyen todas las rutas de los módulos usando include().
- Ejemplo: /api/booking/bookings/ apunta al BookingViewSet.

---

7. Permisos y Roles

- Se usan grupos de Django para definir roles:
    - ADMINISTRADOR: Acceso total a todas las apps.
    - AGENTE_VENTAS: Gestiona cotizaciones y reservas propias.
    - OPERADOR: Ve sus asignaciones y actualiza estado de servicios.
    - CONTADOR: Consulta pagos y reportes.
- Los permisos se aplican en ViewSets con clases personalizadas.

---

8. CRUD de Reservas

1. Crear reserva: POST /api/booking/bookings/
2. Leer reservas: GET /api/booking/bookings/ (usuario ve las suyas, admin todas)
3. Actualizar reserva: PUT/PATCH /api/booking/bookings/{id}/
4. Eliminar reserva: DELETE /api/booking/bookings/{id}/

- El serializer convierte los datos JSON a modelo Booking.
- El ViewSet controla la lógica y los permisos.
- La tabla Booking se almacena en SQLite.

---

9. Testing y API

- Se puede probar la API desde:
    - Interfaz web de Django REST Framework.
    - Postman usando sesión (login) o JWT (token Bearer).

- JWT:
    1. POST /api/auth/token/ con username/password.
    2. Usar access token en encabezado Authorization: Bearer <token> para acceder a la API.

- Ejemplo JSON para crear reserva:
{
  "tour": 1,
  "salida": 1,
  "personas": 2,
  "importe_centavos": 500000,
  "moneda": "usd"
}

---

10. Carpetas especiales

- common/: Código y utilidades compartidas entre módulos.
- use_cases/: Lógica de negocio específica, por ejemplo:
    - Crear reserva con validaciones.
    - Procesar pagos.
    - Generar cotizaciones.

- api/: Endpoints para exponer la funcionalidad de cada módulo.

---

11. Flujo General

1. El usuario inicia sesión o se registra.
2. Consulta tours disponibles y selecciona uno.
3. Crea la reserva y realiza el pago.
4. El operador recibe la asignación y actualiza estado.
5. Los administradores y contadores pueden consultar reportes y métricas.

---

12. Resumen

- models.py → define tablas.
- serializers.py → convierte datos a JSON.
- views.py / viewsets.py → controla lógica CRUD y permisos.
- urls.py → rutas de la API.
- admin.py → gestión en el panel de Django.
- packages/use_cases → lógica de negocio central.
- SQLite → almacena los datos.
- Postman o frontend → consumen la API.
