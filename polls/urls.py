# URLConf of this appp
from django.urls import path

from . import views  # dot "." means current app ( polls )

app_name = "polls"  # namespace for app
urlpatterns = [
    path('', views.index, name="index"),  # mapping to func index() in views.py
    # ex: /polls/5
    path('<int:question_id>/', views.detail, name="detail"),
    # ex: /polls/5/results
    path('<int:question_id>/results/', views.results, name="results"),
    # ex: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name="vote"),
]
