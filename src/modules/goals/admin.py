from django.contrib import admin

# Register your models here.
from .models import Goal, Objective, Plan, Assignment

admin.site.register(Goal)
admin.site.register(Objective)
admin.site.register(Plan)
admin.site.register(Assignment)
