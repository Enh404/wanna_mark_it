from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg, Count
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core.paginator import Paginator

from games.models import User, Game, Category, GameMark, Profile
from games.forms import GameMarkForm, ProfileForm


def index(request):
    gamemark_list = GameMark.objects.all()
    paginator = Paginator(gamemark_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'games/index.html', context)


def category_gamemark(request, slug):
    category = get_object_or_404(Category, slug=slug)
    gamemark_list = GameMark.objects.filter(game__category=category)
    paginator = Paginator(gamemark_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'games/category_gamemark.html', context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    gamemarks_by_user = GameMark.objects.filter(user=user)
    paginator = Paginator(gamemarks_by_user, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'profile': profile,
        'gamemarks_by_user': gamemarks_by_user,
        'page_obj': page_obj,
    }
    return render(request, 'games/profile.html', context)


def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    gamemarks_by_game = GameMark.objects.filter(game=game)
    paginator = Paginator(gamemarks_by_game, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    avg_mark = gamemarks_by_game.aggregate(Avg('mark'))
    context = {
        'game': game,
        'page_obj': page_obj,
        'avg_mark': avg_mark['mark__avg'],
    }
    return render(request, 'games/game_detail.html', context)


def profile_about(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    gamemarks_by_user = GameMark.objects.filter(user=user)
    context = {
        'user': user,
        'profile': profile,
        'gamemarks_by_user': gamemarks_by_user,
    }
    return render(request, 'games/profile_about.html', context)


@login_required
def gamemark_create(request):
    form = GameMarkForm(request.POST or None)
    gamemarks_by_user = GameMark.objects.filter(user=request.user.id)
    if form.is_valid():
        gamemark = form.save(commit=False)
        gamemark.user = request.user
        try:
            gamemark.save()
            game_from_data = form.cleaned_data.get('game')
            game = get_object_or_404(Game, name=game_from_data)
            if gamemarks_by_user.count() == 1:
                return redirect('achievements:first_achievement_received', request.user.id)
            elif gamemarks_by_user.filter(game__category=game.category).count() == 2:
                return redirect('achievements:achievement_received', request.user.id, game.category.slug, 2)
            elif gamemarks_by_user.filter(game__category=game.category).count() == 5:
                return redirect('achievements:achievement_received', request.user.id, game.category.slug, 5)
            elif gamemarks_by_user.filter(game__category=game.category).count() == 10:
                return redirect('achievements:achievement_received', request.user.id, game.category.slug, 10)
            else:
                return redirect('games:profile', request.user.username)
        except IntegrityError:
            form.add_error(None, 'Вы уже ставили оценку этой игре')
    context = {
        'gamemarks_by_user': gamemarks_by_user,
        'form': form,
    }
    return render(request, 'games/create_gamemark.html', context)


@login_required
def gamemark_edit(request, gamemark_id):
    gamemark = get_object_or_404(GameMark, pk=gamemark_id)
    if gamemark.user != request.user:
        return redirect('games:profile', request.user.username)
    form = GameMarkForm(request.POST or None, instance=gamemark)
    if form.is_valid():
        form.save()
        return redirect('games:profile', request.user.username)
    context = {
        'is_edit': True,
        'form': form,
    }
    return render(request, 'games/create_gamemark.html', context)


@login_required
def profile_edit(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if profile.user != request.user:
        return redirect('games:profile', request.user.username)
    form = ProfileForm(request.POST or None, files=request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('games:profile', request.user.username)
    context = {
        'form': form,
    }
    return render(request, 'games/profile_edit.html', context)


def game_rating(request):
    games = Game.objects.all()
    gamemarks_list = GameMark.objects.values('game_id').annotate(avg = Avg('mark')).order_by('-avg')[:10]
    context = {
        'games': games,
        'gamemarks_list': gamemarks_list,
    }
    return render(request, 'games/game_rating.html', context)
