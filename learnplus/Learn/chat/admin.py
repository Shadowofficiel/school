from django.contrib import admin
from .models import Salon, Message, PrivateMessage


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des salons
    list_display = ('nom', 'classe', 'date_add', 'status',)

    # Filtres pour affiner les recherches dans l'admin
    list_filter = ('status',)

    # Champs de recherche
    search_fields = ('nom', 'classe__niveau__nom', 'classe__numeroClasse')

    # Champs non modifiables
    readonly_fields = ('date_add', 'date_upd')

    # Organisation des champs dans les formulaires d'édition
    fieldsets = [
        ('Informations générales', {'fields': ['nom', 'classe', 'status']}),  # Champs modifiables
        ('Dates', {'fields': ['date_add', 'date_upd']}),  # Champs non modifiables
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des messages
    list_display = ('auteur', 'message', 'salon', 'status', 'date_add', 'date_update')

    # Filtres pour affiner les recherches dans l'admin
    list_filter = ('status', 'salon',)

    # Champs de recherche
    search_fields = ('auteur__username', 'message', 'salon__nom')

    # Champs non modifiables
    readonly_fields = ('date_add', 'date_update')

    # Organisation des champs dans les formulaires d'édition
    fieldsets = [
        ('Informations sur le message', {'fields': ['auteur', 'salon', 'message', 'status']}),  # Champs modifiables
        ('Dates', {'fields': ['date_add', 'date_update']}),  # Champs non modifiables
    ]


@admin.register(PrivateMessage)
class PrivateMessageAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste des messages privés
    list_display = ('sender', 'receiver', 'message', 'date_add', 'date_update')

    # Filtres pour affiner les recherches dans l'admin
    list_filter = ('date_add', 'sender', 'receiver')

    # Champs de recherche
    search_fields = ('sender__username', 'receiver__username', 'message')

    # Champs non modifiables
    readonly_fields = ('date_add', 'date_update')

    # Organisation des champs dans les formulaires d'édition
    fieldsets = [
        ('Informations sur l\'expéditeur et le destinataire', {'fields': ['sender', 'receiver']}),  # FK pour sender et receiver
        ('Message', {'fields': ['message']}),  # Champ message
        ('Dates', {'fields': ['date_add', 'date_update']}),  # Champs non modifiables
    ]
