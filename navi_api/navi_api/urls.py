from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schedules/', include('schedules.urls')),
    path('api/routes/', include('routes.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('', include('feedback.urls')),
]
