from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_user, name='add_user'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('read/<int:user_id>/', views.read_user, name='read_user'),
    path('read-all/', views.read_all_users, name='read_all_users'),
    path('read/', views.read_user, name='read_user'),
    path('manage_user/', views.manage_users, name='manage_user'),
]
