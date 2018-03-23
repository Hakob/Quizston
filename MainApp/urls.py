from django.urls import path
from .views import MyView, SignUpView, validate_username

urlpatterns = [
    path('', MyView.as_view(template_name='index.html'), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('ajax/validate_username/', validate_username, name='validate_username'),
]
