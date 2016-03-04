from django.conf.urls import url

from . import views

app_name='app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.TicketView.as_view(), name='ticket'),
]