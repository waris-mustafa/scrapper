from django.contrib import admin
from django.urls import path, include

urlpatterns = [path('admin/', admin.site.urls), path('api/', include('apps.scrape.urls')),
               path('api/', include('apps.auth_.urls')), path('api/', include('apps.email_sender.urls')), ]
