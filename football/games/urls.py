from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.match, name='match'),
    path('<int:match_id>/', views.match_detail, name='match_detail'),
]
