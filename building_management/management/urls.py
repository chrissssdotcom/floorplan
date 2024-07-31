from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('buildings/', views.building_list, name='building_list'),
    path('buildings/add/', views.building_create, name='building_create'),
    path('floors/', views.floor_list, name='floor_list'),
    path('floors/add/', views.floor_create, name='floor_create'),
    path('locations/', views.location_list, name='location_list'),
    path('locations/add/', views.location_create, name='location_create'),
    path('people/', views.person_list, name='person_list'),
    path('people/add/', views.person_create, name='person_create'),
    path('floors/<int:floor_id>/plot/', views.plot_locations, name='plot_locations'),
    path('locations/<int:location_id>/update_coordinates/', views.update_location_coordinates, name='update_location_coordinates'),
]
