from django.contrib import admin

from games.models import Game, Category, GameMark, Profile

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(GameMark)
admin.site.register(Profile)