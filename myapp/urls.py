from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path('function/', views.function_view, name='function_view'),
    path('class/', views.ClassView.as_view(), name='class_view'),
]
