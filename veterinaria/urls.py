"""veterinaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from veterinaria import views

from django_distill import distill_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('identidad/', views.identidad, name="identidad"),
    path('filosofia/', views.filosofia, name="filosofia"),
    path('foda/', views.foda, name="foda"),
    path('servicios/', views.servicios, name="servicios"),
    path('indicadores/', views.indicadores, name="indicadores"),
    path('staff/', views.staff, name="staff"),
    path('acicalamiento/', views.acicalamiento, name="acicalamiento"),
    path('otros/', views.otros, name="otros"),
    path('medico/', views.medico, name="medico"),
]  

""" urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('index.html', views.index, name="index"),
    distill_path('identidad.html', views.identidad, name="identidad"),
    distill_path('filosofia.html', views.filosofia, name="filosofia"),
    distill_path('foda.html', views.foda, name="foda"),
    distill_path('servicios.html', views.servicios, name="servicios"),
    distill_path('indicadores.html', views.indicadores, name="indicadores"),
    distill_path('staff.html', views.staff, name="staff"),
    distill_path('acicalamiento.html', views.acicalamiento, name="acicalamiento"),
    distill_path('otros.html', views.otros, name="otros"),
    distill_path('medico.html', views.medico, name="medico"),
    
] """
 
