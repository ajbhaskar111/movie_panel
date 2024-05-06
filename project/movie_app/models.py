from django.db import models

# Create your models here.
# gener_category =  (
#     ('action', 'Action'),
#     ('romanic', 'Romantic'),
#     ('comedy','Comedy'),
#     ('thriller','Thriller')
# )
class Genre(models.Model):
    Genre_name = models.CharField(default='action', max_length=100)
    class Meta:
        db_table = 'genre'
     
    def __str__(self) -> str:
        return self.Genre_name  

class MovieLIst(models.Model):
    Title = models.CharField(max_length= 200)
    Poster = models.FileField(upload_to='users/avatars', default='avatar.png')
    Genre = models.ForeignKey(Genre,on_delete=models.CASCADE)
    Rating = models.FloatField(max_length= 3)
    Year_release = models.DateField(auto_created=True,)
    Metacritic_rating = models.FloatField(max_length= 3)
    Runtime = models.CharField(max_length= 200)

    class Meta:
        db_table = 'movie_listing'

    def __str__(self) -> str:
        return self.Title    
