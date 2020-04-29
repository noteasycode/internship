from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:route>', views.display_route, name='route'),
]