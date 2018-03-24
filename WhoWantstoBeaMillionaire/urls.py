from django.contrib import admin
from django.urls import include, re_path
from quiz import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^main/', include('MainApp.urls')),
    re_path(r'^quiz/', include('quiz.urls')),

    re_path(r'^login', views.welcome, name="login"),
    re_path(r'^', include('django.contrib.auth.urls')),
    re_path(r'^$', views.welcome, name="home"),

]
