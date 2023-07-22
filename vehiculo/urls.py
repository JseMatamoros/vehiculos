from django.urls import path
# from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.custom_logout, name='logout'),
    path('accounts/login/', views.custom_login, name='login'),
    path('custom_login/', views.custom_login, name='custom_login'),
    path('vehiculo/add/', views.vehiculo_add, name='vehiculo_add'),
    path('vehiculo/list/', views.vehiculo_list, name='vehiculo_list'),
    path('vehiculo/administrar/', views.administrar_vehiculos, name='administrar'),
    path('vehiculo/modificar/<int:pk>/', views.modificar_vehiculo, name='modificar_vehiculo'),
    path('vehiculo/eliminar/<int:pk>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
]
