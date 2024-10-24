from django.urls import re_path
from .views import NotificationAPIView

urlpatterns = [
    re_path(r'^notification/?$', NotificationAPIView.as_view(), name='create-notification'),
]
