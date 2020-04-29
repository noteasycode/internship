from django.urls import path
from locations import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_with_arg/<str:add_something>', views.index_with_arg),
]