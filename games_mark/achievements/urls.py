from django.urls import path

from . import views

app_name = 'achievements'

urlpatterns = [
    path('achievements/<int:user_id>/', views.achievement_received, name='achievement_received'),
]