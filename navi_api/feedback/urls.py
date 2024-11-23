from django.urls import path
from . import views


urlpatterns = [
    path('', views.feedback_form, name='feedback_form'),  # This will render the feedback form at /feedback/
     path('submit', views.add_feedback, name='add_feedback'),
]
