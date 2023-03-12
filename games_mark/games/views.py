from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from games.models import User, Game, Category, GameMark


def index(request):
    gamemark_list = GameMark.objects.all()
    context = {
        'gamemark_list': gamemark_list,
    }
    return render(request, 'games/index.html', context)


def category_gamemark(request, slug):
    category = get_object_or_404(Category, slug=slug)
    gamemark_list = GameMark.objects.filter(game__category=category)
    context = {
        'category': category,
        'gamemark_list': gamemark_list,
    }
    return render(request, 'games/category_gamemark.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    gamemarks_by_user = GameMark.objects.filter(user=user)
    context = {
        'user': user,
        'gamemarks_by_user': gamemarks_by_user,
    }
    return render(request, 'games/profile.html', context)


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    gamemarks_by_game = GameMark.objects.filter(game=game).aggregate(Avg('mark'))
    context = {
        'game': game,
        'gamemarks_by_game': gamemarks_by_game['mark__avg'],
    }
    return render(request, 'games/game_detail.html', context) 