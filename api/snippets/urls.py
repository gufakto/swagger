from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url('home', views.Home.as_view()),
    url(r'^$', schema_view)
]
