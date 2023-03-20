from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from achievements.models import Achievement


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='games',
    )
    year = models.PositiveSmallIntegerField(
        # validators=[year_validator, ]
    )

    def __str__(self):
        return self.name

class GameMark(models.Model):
    comment = models.TextField()
    game = models.ForeignKey(
        Game, 
        on_delete=models.CASCADE,
        related_name='gamemarks'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='gamemarks')
    mark = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    
    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return f'{self.game.name}, {self.mark}'


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    about = models.TextField(null=True, blank=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profile/')
    achievements = models.ManyToManyField(
        Achievement,
        related_name='profiles',
        blank=True,
    )
    
    def __str__(self):
        return self.user.username
