"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def root(request):
    return JsonResponse({"status": "ok", "api": ["/admin/", "/api/booking/"]})

urlpatterns = [
    path("", root),  # ← ahora / responde algo
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/booking/", include("packages.reservas_pagos.api.urls")),
    path("api/auth/", include("accounts.api_urls")),
]