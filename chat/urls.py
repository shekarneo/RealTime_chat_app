from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^chat/$', views.index, name='index'),
    url(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]