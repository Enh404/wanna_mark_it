from django.shortcuts import render, get_object_or_404

from achievements.models import Achievement
from games.models import Profile
from core.check_achievement import check_achievement


def first_achievement_received(request, user_id):
    profile = get_object_or_404(Profile, user=user_id)
    achievement = get_object_or_404(Achievement, id=1)
    Profile.objects.get(user=user_id).achievements.add(achievement)
    context = {
        'profile': profile,
        'achievement': achievement,
    }
    return render(request, 'achievements/achievement_received.html', context)


def achievement_received(request, user_id, slug, count):
    profile = get_object_or_404(Profile, user=user_id)
    achievement = get_object_or_404(Achievement, id=check_achievement(slug, count))
    Profile.objects.get(user=user_id).achievements.add(achievement)
    context = {
        'profile': profile,
        'achievement': achievement,
    }
    return render(request, 'achievements/achievement_received.html', context)