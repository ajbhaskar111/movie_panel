from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

index_html = "index.html"

def index(request):
    # return HttpResponse("<h2>Hello Python</h2>")
 
    # context['product_list'] = MovieLIst.objects.all().filter(Title = request.POST['search'])
    MovideData = MovieLIst.objects.all() 
    genreID = request.GET.get("genre") 
    if request.method == "GET":
        st = request.GET.get('search')
        if st != None:
            MovideData = MovieLIst.objects.filter(Title__icontains= st)
        elif genreID:
            MovideData = MovieLIst.objects.filter(Genre = genreID)
        else:
             MovideData = MovieLIst.objects.all() 
        genre_data = Genre.objects.all()
    data = {
       'data_show' : MovideData,
       'genre_list' : genre_data
    }
    return render(request,index_html,data)



