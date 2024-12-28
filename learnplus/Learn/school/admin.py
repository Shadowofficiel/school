from django.contrib import admin
from . import models


class CustomAdmin(admin.ModelAdmin):
    actions = ('activate', 'desactivate')
    list_filter = ('status',)
    list_per_page = 10

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activée avec succès.')
    activate.short_description = "Activer les éléments sélectionnés"

    def desactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivée avec succès.')
    desactivate.short_description = "Désactiver les éléments sélectionnés"


class FiliereAdmin(CustomAdmin):
    list_display = ('nom', 'status', 'date_add')
    search_fields = ('nom',)
    fieldsets = [
        ("Informations", {"fields": ["nom", "description", "niveaux"]}),
        ("Standard", {"fields": ["status"]}),
    ]


class MatiereAdmin(CustomAdmin):
    list_display = ('nom', 'filiere', 'status')
    search_fields = ('nom',)
    fieldsets = [
        ("Informations", {"fields": ["nom", "image", "description", "filiere"]}),
        ("Standard", {"fields": ["status"]}),
    ]


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Filiere, FiliereAdmin)
_register(models.Matiere, MatiereAdmin)
_register(models.Niveau, CustomAdmin)
_register(models.Classe, CustomAdmin)
_register(models.Chapitre, CustomAdmin)
_register(models.Cours, CustomAdmin)
