from django.conf.urls import url

from gunosynews import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
