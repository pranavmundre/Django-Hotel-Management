from django.urls import path

from.import views

urlpatterns = [
    path('', views.index, name='Dashboard'),
    path('rooms/', views.rooms, name='Rooms'),
    path('rooms/add-room', views.addRoom, name='Add Room'),
    path('room/edit/<int:get_room_no>/', views.editRoom, name='Edit Room'),
    path('booking-details/', views.bookingDetails, name='Booking Details'),
    path('profile/', views.profile, name='Profile'),
    # path('user-registration/', views.rooms, name='rooms'),
    # path('rooms/', views.rooms, name='rooms'),



    # ---- AJAX ----#

    path('get-room-details/', views.getRoomDetails, name='getRoomDetails'),
    path('save-room-details/', views.SaveRoomDetails, name='SaveRoomDetails'),
    path('data-table-ajax/', views.dataTableAjax, name='dataTableAjax'),

]