from django.conf.urls import url
from . import views           # Import views from current directory

urlpatterns = [
	url(r'^$', views.index),     # Linking to views.index #Remember commas!!
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
] #Remember closing bracket!!
