from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='login_index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.createUser, name='register'),
]