from django.contrib import admin

# Register your models here.
from .models import Project, Skill

admin.site.register(Project)
admin.site.register(Skill)
