from django.contrib import admin
from .models import *
# Register your models here.
class ShowMovie_list(admin.ModelAdmin):
    list_display = ["Title", "Poster", "Genre" , "Rating" , "Year_release" , "Metacritic_rating" ,"Runtime"]

class Gener_list(admin.ModelAdmin):
    list_display = ["id", "Genre_name"]

admin.site.register(MovieLIst,ShowMovie_list)
admin.site.register(Genre,Gener_list)

