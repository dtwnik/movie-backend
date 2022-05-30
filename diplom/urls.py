from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/', include('cinema.urls')),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
              ]
