from django.contrib import admin
from .models import Team, Man

class TeamAdmin(admin.ModelAdmin):
  list_display = ("name",)

admin.site.register(Team, TeamAdmin)
admin.site.register(Man)
