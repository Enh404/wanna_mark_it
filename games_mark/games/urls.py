from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_gamemark, name='category_gamemark'),
]