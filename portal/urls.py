from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add_user, name='add_user'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('search/<int:user_id>/', views.read_user, name='read_user'),
    path('read-all/', views.read_all_users, name='read_all_users'),
    path('search/', views.search_user, name='search-user'),
]
