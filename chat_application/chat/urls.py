from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('save', views.save, name='save'),
    path('get_name/', views.get_name, name='get_name'),
]
