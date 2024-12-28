from django.contrib import admin
from . import models

class CustomAdmin(admin.ModelAdmin):
    actions = ('activate', 'desactivate')
    list_filter = ('status',)
    list_per_page = 10
    date_hierachy = "date_add"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La sélection a été activée avec succès.')
    activate.short_description = "Activer les champs sélectionnés"

    def desactivate(self, request, queryset):  
        queryset.update(status=False)
        self.message_user(request, 'La sélection a été désactivée avec succès.')
    desactivate.short_description = "Désactiver les champs sélectionnés"

class QuestionAdmin(CustomAdmin):
    list_display = ('quiz', 'typequestion', 'point', 'status')
    list_display_links = ['typequestion']
    search_fields = ('typequestion', 'quiz__titre')
    fieldsets = [
        ("Info Question", {"fields": ["typequestion", "point", "quiz", "question"]}),
        ("Standard", {"fields": ["status"]})
    ]

class ReponseAdmin(CustomAdmin):
    list_display = ('reponse', 'question', 'is_True', 'status')
    list_display_links = ['reponse']
    search_fields = ('reponse',)
    fieldsets = [
        ("Info Réponse", {"fields": ["reponse", "question", "is_True"]}),
        ("Standard", {"fields": ["status"]})
    ]

class QuizAdmin(CustomAdmin):
    list_display = ('date', 'titre', 'temps', 'status')
    list_display_links = ['titre']
    search_fields = ('titre',)
    fieldsets = [
        ("Info Quiz", {"fields": ["date", "titre", "cours", "temps"]}),
        ("Standard", {"fields": ["status"]})
    ]

class DevoirAdmin(CustomAdmin):
    list_display = ('dateDebut', 'dateFermeture', 'chapitre', 'coefficient', 'support', 'status')
    list_display_links = ('chapitre',)
    search_fields = ('chapitre',)
    fieldsets = [
        ("Info Devoir", {"fields": ["dateDebut", "dateFermeture", 'chapitre', 'support']}),
        ("Standard", {"fields": ["status"]})
    ]


class StudentAnswerAdmin(CustomAdmin):
    list_display = ('get_user', 'get_quiz', 'question', 'selected_answer', 'is_correct', 'points_earned', 'status')
    list_display_links = ('get_user', 'get_quiz', 'question')
    search_fields = ('quiz_result__user__username', 'quiz_result__quiz__titre', 'question__question')
    list_filter = ('is_correct', 'status', 'quiz_result__quiz')

    fieldsets = [
        ("Info Student Answer", {
            "fields": ["quiz_result", "question", "selected_answer", "is_correct", "points_earned"]
        }),
        ("Standard", {"fields": ["status"]})
    ]

    def get_user(self, obj):
        return obj.quiz_result.user.username
    get_user.short_description = "Étudiant"

    def get_quiz(self, obj):
        return obj.quiz_result.quiz.titre
    get_quiz.short_description = "Quiz"


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.Question, QuestionAdmin)
_register(models.Reponse, ReponseAdmin)
_register(models.Quiz, QuizAdmin)
_register(models.Devoir, DevoirAdmin)
_register(models.StudentAnswer, StudentAnswerAdmin)
