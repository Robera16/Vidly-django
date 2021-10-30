from django.http import HttpResponse
from django.shortcuts import render

from movies.admin import MovieAdmin
from .models import Movie

# Create your views here.

def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

