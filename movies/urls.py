from django.urls import path
from django.urls import path
from . import views
# mapping a url endpoint to view function

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]