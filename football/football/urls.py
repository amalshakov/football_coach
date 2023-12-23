from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
