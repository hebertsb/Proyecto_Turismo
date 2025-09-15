Condominio Inteligente – Primer Parcial
1. Introducción

Este proyecto es una plataforma de gestión de condominios con inteligencia artificial, accesible tanto desde web como desde dispositivos móviles.
Su objetivo principal es optimizar la administración y la experiencia de los residentes mediante automatización y análisis inteligente de datos.
Funciones principales para los usuarios:
Reservar y gestionar áreas comunes (salones, parqueos, canchas, etc.).
Pagar cuotas y servicios en línea de manera segura.
Recibir notificaciones inteligentes (recordatorios de pagos, alertas de seguridad, avisos del condominio).
Asistencia virtual con IA para consultas frecuentes de residentes.
Funciones para administradores:
Gestión de residentes y personal (roles, accesos y permisos).
Control de pagos, reportes y balances.
Supervisión de reservas y mantenimiento preventivo.
Panel con analítica predictiva (detección de morosidad, consumo de servicios, optimización de recursos).
Tecnologías utilizadas:

Backend: Django
Base de Datos: SQLite
Frontend Web/Móvil: React / Flutter
IA: Modelos integrados para recomendaciones y análisis predictivo.

2. Estructura General del Proyecto
2.1 Carpeta sitio/

Configuración global de Django.

Archivos clave:

settings.py: Configuración de base de datos, apps, middleware y autenticación.
urls.py: Rutas principales del proyecto.
wsgi.py: Configuración para despliegue en producción.

2.2 Apps principales

accounts/: Gestión de usuarios, roles, accesos y autenticación.
reservas/: Reservas de áreas comunes y control de disponibilidad.
pagos/: Procesamiento de pagos de cuotas, mantenimiento y servicios.
reportes/: Generación de reportes administrativos y financieros.
personal/: Administración de personal de seguridad, limpieza y mantenimiento.
notificaciones/: Sistema de alertas, recordatorios y comunicados.
ia/: Módulo de inteligencia artificial para predicciones y asistencia virtual.
core/: Entidades centrales como Condominio, UnidadHabitacional, Residentes.

2.3 Carpeta packages/

Código reutilizable y casos de uso.

Ejemplos:

reservas_pagos/: Gestión integrada de reservas con pagos.
analitica/: Modelos predictivos para consumos y morosidad.
mantenimiento/: Lógica para control de mantenimientos programados.

3. Modelos y Base de Datos

Algunos modelos principales:

UnidadHabitacional: Representa cada departamento o casa.
Residente: Información del propietario o inquilino.
Reserva: Gestión de áreas comunes (fecha, estado, usuario).
Pago: Registro de cuotas, servicios y estado de pago.
Notificación: Avisos enviados al residente.
El ORM de Django transforma estos modelos en tablas en SQLite.

4. Serializadores (serializers.py)

Transforman datos entre modelos Django y JSON.
Ejemplo: ReservaSerializer convierte los datos de una reserva en JSON para la API.

5. Vistas y ViewSets (views.py / viewsets.py)

Cada módulo tiene su ViewSet CRUD:

ReservaViewSet: Crear, leer, actualizar y cancelar reservas.
PagoViewSet: Procesar pagos y consultar estados.
Permisos integrados para garantizar seguridad según el rol del usuario.

6. Rutas y URLs (urls.py)

Cada app define sus rutas internas.
En sitio/urls.py se integran todas.
Ejemplo: /api/reservas/ apunta al ReservaViewSet.

7. Permisos y Roles

ADMINISTRADOR: Acceso total.
COPROPIETARIO: Puede gestionar su unidad, pagos y reservas.
SERVICIOS: Solo accede a sus tareas asignadas.
PERSONAL: Consulta reportes financieros y pagos.

8. CRUD de Reservas

Crear: POST /api/reservas/
Leer: GET /api/reservas/
Actualizar: PUT/PATCH /api/reservas/{id}/
Eliminar: DELETE /api/reservas/{id}/

9. Testing y API

Pruebas con:
Django REST Framework
Postman
JWT para autenticación de usuarios.
Ejemplo JSON de reserva:

{
  "area": 1,
  "fecha": "2025-09-15",
  "hora_inicio": "18:00",
  "hora_fin": "20:00",
  "residente": 3
}

10. Carpetas Especiales

common/: Código compartido.
use_cases/: Casos de negocio específicos (ej. predicción de pagos atrasados).
api/: Endpoints expuestos para cada módulo.

11. Flujo General del Sistema

Residente inicia sesión.
Consulta su estado de cuenta y reserva áreas comunes.
Realiza pago online.
El sistema con IA sugiere recordatorios y predicciones.
Administradores consultan reportes y métricas.

12. Resumen

models.py → define las tablas.
serializers.py → transforma a JSON.
views.py / viewsets.py → CRUD y permisos.
urls.py → rutas API.
ia/ → lógica de inteligencia artificial.
SQLite → base de datos.
Postman o frontend → consumen la API.
