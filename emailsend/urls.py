from django.urls import re_path
from .views import SendEmailView

urlpatterns = [
    re_path(r'^send-email/?$', SendEmailView.as_view(), name='send-email'),
]