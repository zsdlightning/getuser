from django.conf.urls import patterns, url

from getuser import views

urlpatterns = patterns('',
    # ex: /getuser/
    url(r'^$', views.index, name='index'),
)
