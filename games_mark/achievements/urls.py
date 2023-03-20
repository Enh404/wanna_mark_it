from django.urls import path

from . import views

app_name = 'achievements'

urlpatterns = [
    path('achievements/<int:user_id>/', views.first_achievement_received, name='first_achievement_received'),
    path('achievements/<int:user_id>/<slug:slug>/<int:count>', views.achievement_received, name='achievement_received'),
]