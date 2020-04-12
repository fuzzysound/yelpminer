"""
URL assignment of the app.
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views

urlpatterns = [
    path('', views.query_result, name="query_es"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=["json", "api"])