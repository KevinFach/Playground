from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('<int:day>', views.days_weeks_with_number),
    path('<str:day>', views.days_weeks, name='day-quote')
]