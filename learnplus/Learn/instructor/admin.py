from django.contrib import admin
from .models import Instructor, AffectationMatiere
from django.utils.safestring import mark_safe
from django import forms

# Classe générique personnalisée
class CustomAdmin(admin.ModelAdmin):
    actions = ('activate', 'desactivate')
    list_filter = ('status',)
    list_per_page = 6
    date_hierachy = "date_add"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activée avec succès.')
    activate.short_description = "Activer les champs sélectionnés"

    def desactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivée avec succès.')
    desactivate.short_description = "Désactiver les champs sélectionnés"

# Administration des instructeurs
class InstructorAdmin(CustomAdmin):
    list_display = ('user', 'contact', 'adresse', 'image_view', 'classe', 'status')
    search_fields = ('user',)
    ordering = ['user']
    list_display_links = ['user']
    fieldsets = [
        ("Info instructeur", {"fields": ["user", "contact", "adresse", "classe", "photo"]}),
        ("Standard", {"fields": ["status"]})
    ]

    def image_view(self, obj):
        return mark_safe(f"<img src='{obj.photo.url}' width='100px' height='50px'>")
    image_view.short_description = "Image"

# Formulaire personnalisé pour filtrer uniquement les instructeurs
class AffectationMatiereForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrer le champ 'instructor' pour n'afficher que les instructeurs
        self.fields['instructor'].queryset = Instructor.objects.filter(status=True)

    class Meta:
        model = AffectationMatiere
        fields = '__all__'

# Administration des affectations de matières
@admin.register(AffectationMatiere)
class AffectationMatiereAdmin(admin.ModelAdmin):
    form = AffectationMatiereForm
    list_display = ('instructor', 'matiere', 'date_assigned')
    search_fields = ('instructor__user__username', 'matiere__nom')
    list_filter = ('date_assigned',)

# Enregistrement des modèles
admin.site.register(Instructor, InstructorAdmin)
