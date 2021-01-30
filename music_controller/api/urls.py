from django.urls import path
from . import views

urlpatterns = [
    path('', views.RoomListView.as_view(), name='list'), 
    path('create/', views.RoomCreateView.as_view(), name='create')
]