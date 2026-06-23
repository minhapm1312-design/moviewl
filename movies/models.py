from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):

    WATCH_STATUS = [
        ('watched', 'Watched'),
        ('not_watched', 'Not Watched'),
        ('dropped', 'Dropped'),
    ]

    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Comedy', 'Comedy'),
        ('Crime', 'Crime'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)

    watch_status = models.CharField(
        max_length=20,
        choices=WATCH_STATUS,
        default='not_watched'
    )

    rating = models.IntegerField(default=0)

    review = models.TextField(blank=True)

    def __str__(self):
        return self.title