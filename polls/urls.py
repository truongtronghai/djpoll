# URLConf of this appp
from django.urls import path

from . import views  # dot "." means current app ( polls )

urlpatterns = [
    path('', views.index, name="index")  # mapping to func index() in views.py
]
