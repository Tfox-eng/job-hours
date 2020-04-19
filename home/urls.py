from django.conf.urls import url
from home.views import HomeView
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    # url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]
