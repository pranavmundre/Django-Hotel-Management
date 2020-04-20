from django.urls import path

from.import views

urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('rooms/', views.rooms, name='Rooms'),
    path('settings/', views.settings, name='settings'),
    path('settings/password/', views.password, name='password'),

]