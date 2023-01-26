from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="test"),
    re_path(r'^generate/$',views.generate, name="generate")
]