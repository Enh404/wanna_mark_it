from django.shortcuts import render, get_object_or_404

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