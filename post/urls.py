from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    # ex: /post/5
    path('<int:question_id>/', views.detail, name="detail"),
]
