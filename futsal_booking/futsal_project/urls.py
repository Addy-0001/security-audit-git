"""
URL configuration for futsal_project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('bookings.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

# Custom admin site configuration
admin.site.site_header = "Futsal Booking Administration"
admin.site.site_title = "Futsal Booking Admin"
admin.site.index_title = "Welcome to Futsal Booking Admin Panel"
