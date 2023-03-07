from django.shortcuts import render

from games.models import User, Game, Category, GameMark


def index(request):
    gamemark_list = GameMark.objects.all()
    context = {
        'gamemark_list': gamemark_list,
    }
    return render(request, 'index.html', context)
