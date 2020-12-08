from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Improving DJ Admin
admin.site.site_title = 'AM6 Site Admin'
admin.site.site_header = 'AM6 Administration'
admin.site.index_title = 'AM6 Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)