
from django.conf.urls import patterns, url
from skeleton.example import views

urlpatterns = patterns('',
    url(r'^/', views.index),
)

