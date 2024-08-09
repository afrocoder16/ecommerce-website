from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  # This is the URL routing system for the entire app
    path('admin/', admin.site.urls),  # admin page
    path('', include('projects.urls')),  # getting all the pages from projects
    path('accounts/', include('django.contrib.auth.urls')),  # This includes default auth URLs
    path('test-api/', test_api, name='test_api'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)