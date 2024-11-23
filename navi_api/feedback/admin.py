from django.contrib import admin
from .models import Feedback


# Register the Feedback model to be visible in the admin interface
admin.site.register(Feedback)