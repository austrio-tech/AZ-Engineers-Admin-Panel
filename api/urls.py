from django.urls import path
from .views import ChangeUserStatusView

urlpatterns = [
    # Add the URL pattern for changing user status
    path('change-status/<int:user_id>/<int:new_status>/', ChangeUserStatusView.as_view(), name='change-user-status'),
]
