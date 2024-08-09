from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from projects.views import test_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('test-api/', test_api, name='test_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
