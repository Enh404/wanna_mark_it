from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_gamemark, name='category_gamemark'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('profile/<str:username>/about/', views.profile_about, name='profile_about'),
    path('create/', views.gamemark_create, name='gamemark_create'),
    path('games/<int:gamemark_id>/edit/', views.gamemark_edit, name='gamemark_edit'),
    path('profile/<int:profile_id>/edit/', views.profile_edit, name='profile_edit'),
    path('game_rating/', views.game_rating, name='game_rating'),
]