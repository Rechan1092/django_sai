from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('group/<int:pk>/', views.group_detail, name='group_detail'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('groupmember/<int:pk>/', views.groupmember_detail, name='groupmember_detail'),
    path('search/', views.search, name='search'),
]
