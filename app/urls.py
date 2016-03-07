from django.conf.urls import url

from . import views

app_name='app'  #ESPACIO DE NOMBRES

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^formularioT/$', views.addTicket, name='formularioT'),
    url(r'^(?P<pk>[0-9]+)/formularioC/$', views.addComment, name='formularioC'),
    url(r'^(?P<pk>[0-9]+)/$', views.TicketView.as_view(), name='ticket'),
]