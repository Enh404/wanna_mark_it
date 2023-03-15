from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

from games.models import User, Game, Category, GameMark, Profile
from games.forms import GameMarkForm, ProfileForm


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
    profile = get_object_or_404(Profile, user=user)
    gamemarks_by_user = GameMark.objects.filter(user=user)
    context = {
        'user': user,
        'profile': profile,
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
    if form.is_valid():
        gamemark = form.save(commit=False)
        gamemark.user = request.user
        gamemark.save()
        return redirect('games:profile', request.user.username)
    context = {
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
