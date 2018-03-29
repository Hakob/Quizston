from django.conf.urls import url, include
from quiz import views

from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.welcome, name="welcome"),
    url(r'^create/', views.create_user, name="create_user"),
    url(r'^validate_login/', views.log_in, name="log_user"),
    url(r'^add_exam/', views.add_exam, name="add_exam"),
    url(r'^test', views.get_data, name="getdata"),
    url(r'^logout', views.log_out, name="log_out"),
    url(r'^validate_username/', views.validate_username, name='validate_username'),

]
