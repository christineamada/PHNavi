from django.urls import path
from .views import RouteListView

urlpatterns = [
    path('route-list', RouteListView.as_view(), name='route-list'),
]
