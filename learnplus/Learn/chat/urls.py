from django.urls import path
from . import views

urlpatterns = [
     path('messages/<str:classe>/', views.messages, name='instructor-messages'),
     path('private-chat/<int:student_id>/', views.private_chat, name='private-chat'),
     
    # path('deconnexion', views.deconnexion, name="deconnexion"),
]