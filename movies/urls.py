from django.urls import path
from django.urls import path
from . import views
# mapping a url endpoint to view function
urlpatterns = [
    path('', views.index, name='index') 
]