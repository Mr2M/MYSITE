from django.urls import path
from website.views import *





urlpatterns = [
path('http',http_view,name='htpp'),
]