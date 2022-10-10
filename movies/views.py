from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse


def about_us(request):
    # return HttpResponse('movies about us')
    return render(request, 'about-us.html')


# Create your views here.
def movies(request):
    movie_all = Movie.objects.all()
    return render(request, 'movie.html', {'movies': movie_all})
