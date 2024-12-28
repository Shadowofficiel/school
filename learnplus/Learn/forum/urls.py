from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_forum, name='create-forum'),
    path('<slug:slug>/', views.forum_detail, name='forum-detail'),
    path('<slug:slug>/add-response/', views.add_response, name='add-response'),
]
