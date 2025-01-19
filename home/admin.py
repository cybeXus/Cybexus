from django.contrib import admin
from .models import Formation

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_creation', 'video')
    search_fields = ('titre',)

