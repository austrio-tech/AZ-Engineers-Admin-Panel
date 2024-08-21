from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('manage_user/', views.manage_user, name='manage_user'),
    path('add-user/', views.add_user, name='add_user'),
    path('update-user/<int:user_id>/', views.update_user, name='update_user'),
    path('read-user/<int:user_id>/', views.read_user, name='read_user'),
    path('read-all-users/', views.read_all_users, name='read_all_users'),
    path('read-user/', views.read_user, name='read_user'),

    path('manage_award/', views.manage_award, name='manage_award'),
    path('add-award/', views.add_award, name='add_award'),
    path('update-award/<int:award_id>/', views.update_award, name='update_award'),
    path('read-award/<int:award_id>/', views.read_award, name='read_award'),
    path('read-all-awards/', views.read_all_awards, name='read_all_awards'),
    path('read-award/', views.read_award, name='read_award'),

    path('manage_client/', views.manage_client, name='manage_client'),
    # path('add-client/', views.add_client, name='add_client'),
    # path('update-client/<int:client_id>/', views.update_client, name='update_client'),
    # path('read-client/<int:client_id>/', views.read_client, name='read_client'),
    # path('read-all-clients/', views.read_all_clients, name='read_all_clients'),
    # path('read-client/', views.read_client, name='read_client'),

    path('manage_project/', views.manage_project, name='manage_project'),

    path('manage_service/', views.manage_service, name='manage_service'),

]
