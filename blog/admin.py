from django.contrib import admin
from portfolio.models import Project
from .models import Blog

admin.site.register(Project)
admin.site.register(Blog)
