"""
URL assignment of the app.
"""
from django.urls import path
from ui import views

urlpatterns = [
    path('', views.YelpminerView.as_view()),
]