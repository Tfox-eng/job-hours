from django.conf.urls import url
from home.views import UserPost_create_view
from . import views
from django.urls import path

urlpatterns = [
    path('form/', UserPost_create_view)
    # path('', views.UserPost_create_view.as_view(), name='home'),
    # url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]