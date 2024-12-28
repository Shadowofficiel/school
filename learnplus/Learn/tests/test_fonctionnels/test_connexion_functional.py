import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_with_empty_fields(client):
    # Test de soumission avec des champs vides
    response = client.post(reverse('login'), {"username": "", "password": ""})
    assert response.status_code == 200
    assert b"Ce champ est obligatoire." in response.content

@pytest.mark.django_db
def test_login_with_only_password(client):
    # Test de soumission avec seulement le mot de passe
    response = client.post(reverse('login'), {"username": "", "password": "1234"})
    assert response.status_code == 200
    assert b"Ce champ est obligatoire." in response.content

@pytest.mark.django_db
def test_login_with_invalid_username(client):
    # Test de soumission avec un nom d'utilisateur invalide
    response = client.post(reverse('login'), {"username": "invalide", "password": "1234"})
    assert response.status_code == 200
    assert b"Veuillez entrer un nom d'utilisateur et un mot de passe valides." in response.content

@pytest.mark.django_db
def test_login_with_valid_credentials(client):
    # Test de soumission avec des identifiants valides
    User.objects.create_user(username="etudiant1", password="1234")
    response = client.post(reverse('login'), {"username": "etudiant1", "password": "1234"})
    assert response.status_code == 302  # Redirection après connexion réussie
    assert response.url == reverse('dashboard')  # Redirection vers le tableau de bord
