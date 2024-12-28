import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_page_access(client):
    # Test si la page de connexion est accessible
    response = client.get(reverse('login'))
    assert response.status_code == 200
    assert b"Connexion" in response.content

@pytest.mark.django_db
def test_login_with_empty_fields(client):
    # Test de soumission avec des champs vides
    response = client.post(reverse('login'), {"username": "", "password": ""})
    assert response.status_code == 200
    assert b"Ce champ est obligatoire." in response.content

@pytest.mark.django_db
def test_login_with_invalid_credentials(client):
    # Test de soumission avec des identifiants incorrects
    response = client.post(reverse('login'), {"username": "wronguser", "password": "wrongpass"})
    assert response.status_code == 200
    assert b"Veuillez entrer un nom d'utilisateur et un mot de passe valides." in response.content

@pytest.mark.django_db
def test_login_with_valid_credentials(client):
    # Test de soumission avec des identifiants valides
    user = User.objects.create_user(username="validuser", password="validpass")
    response = client.post(reverse('login'), {"username": "validuser", "password": "validpass"})
    assert response.status_code == 302  # Redirection après connexion
    assert response.url == reverse('dashboard')  # Redirection vers le tableau de bord

from quiz.models import Quiz

@pytest.mark.django_db
def test_quiz_list_view(client):
    # Crée des quizzes pour le test
    Quiz.objects.create(title="Quiz 1", description="Description du Quiz 1")
    Quiz.objects.create(title="Quiz 2", description="Description du Quiz 2")
    response = client.get(reverse('quiz_list'))
    assert response.status_code == 200
    assert b"Quiz 1" in response.content
    assert b"Quiz 2" in response.content

@pytest.mark.django_db
def test_quiz_detail_view(client):
    quiz = Quiz.objects.create(title="Quiz Test", description="Description du quiz de test")
    response = client.get(reverse('quiz_detail', args=[quiz.id]))
    assert response.status_code == 200
    assert b"Quiz Test" in response.content

@pytest.mark.django_db
def test_quiz_create_view(client):
    data = {'title': 'Nouveau Quiz', 'description': 'Description pour le nouveau quiz'}
    response = client.post(reverse('quiz_create'), data)
    assert response.status_code == 302
    assert Quiz.objects.filter(title="Nouveau Quiz").exists()

@pytest.mark.django_db
def test_quiz_update_view(client):
    quiz = Quiz.objects.create(title="Ancien Titre", description="Ancienne Description")
    data = {'title': 'Titre Mis à Jour', 'description': 'Description Mise à Jour'}
    response = client.post(reverse('quiz_update', args=[quiz.id]), data)
    assert response.status_code == 302
    quiz.refresh_from_db()
    assert quiz.title == "Titre Mis à Jour"

@pytest.mark.django_db
def test_quiz_delete_view(client):
    quiz = Quiz.objects.create(title="Quiz à Supprimer", description="Description à Supprimer")
    response = client.post(reverse('quiz_delete', args=[quiz.id]))
    assert response.status_code == 302
    assert not Quiz.objects.filter(id=quiz.id).exists()
