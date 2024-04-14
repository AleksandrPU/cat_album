from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from cats.views import AchievementViewSet, CatViewSet

router = routers.DefaultRouter()
router.register('cats', CatViewSet)
router.register('achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
