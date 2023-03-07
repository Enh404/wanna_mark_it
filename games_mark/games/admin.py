from django.contrib import admin

from games.models import Game, Category, GameMark

admin.site.register(Category)
admin.site.register(Game)
admin.site.register(GameMark)