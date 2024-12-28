from django.contrib import admin
from .models import Sujet, Reponse

@admin.register(Sujet)
class SujetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'user', 'cours', 'date_add', 'status')
    search_fields = ('titre', 'user__username', 'cours__titre')
    list_filter = ('status', 'date_add')

@admin.register(Reponse)
class ReponseAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'user', 'reponse', 'date_add', 'status')
    search_fields = ('sujet__titre', 'user__username')
    list_filter = ('status', 'date_add')
