from django.urls import path
from . import views


urlpatterns = [
    path('',views.home , name="home"),
    path('room/<str:id>',views.room , name="room"),
    path('create-room/',views.createRoom , name="create-room"),
    path('update-room/<str:id>',views.updateRoom , name="update-room"),
    path('delete-room/<str:id>',views.deleteRoom , name="delete-room")
]