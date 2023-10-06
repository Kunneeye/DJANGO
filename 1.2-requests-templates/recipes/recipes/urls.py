from django.urls import path, re_path, include
from calculator.views import menu_views, recipe_views

urlpatterns = [
    path('',menu_views),
    re_path(r".", recipe_views)
]
