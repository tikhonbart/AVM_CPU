from django.urls import path, include
from main.views import *

urlpatterns = [
    path('', index, name="home"),
    path('controllerInfo/', viewBlocks, name="blockview")    # http://127.0.0.1:8000/main/controllerInfo
]