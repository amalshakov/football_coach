from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('teams.urls', namespace='teams')),
    path('match/', include('games.urls', namespace='games')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    # path('about/', include('about.urls', namespace='about')),
]
