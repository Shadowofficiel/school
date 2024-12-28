# test_forms.py

import pytest
from Learn.forms import QuizForm

@pytest.mark.django_db
def test_quiz_form_valid():
    # Teste si un formulaire de quiz avec des données valides est valide
    form_data = {
        "title": "Test Quiz",
        "description": "Description pour le test du formulaire."
    }
    form = QuizForm(data=form_data)
    assert form.is_valid(), "Le formulaire devrait être valide avec des données correctes."

@pytest.mark.django_db
def test_quiz_form_invalid_missing_title():
    # Teste si un formulaire de quiz sans titre est invalide
    form_data = {
        "title": "",
        "description": "Description sans titre."
    }
    form = QuizForm(data=form_data)
    assert not form.is_valid(), "Le formulaire ne devrait pas être valide sans titre."

@pytest.mark.django_db
def test_quiz_form_invalid_missing_description():
    # Teste si un formulaire de quiz sans description est invalide
    form_data = {
        "title": "Quiz sans description",
        "description": ""
    }
    form = QuizForm(data=form_data)
    assert not form.is_valid(), "Le formulaire ne devrait pas être valide sans description."

@pytest.mark.django_db
def test_quiz_form_partial_data():
    # Teste si un formulaire avec des données partielles est invalide
    form_data = {"title": "Titre partiel"}  # Pas de description
    form = QuizForm(data=form_data)
    assert not form.is_valid(), "Le formulaire ne devrait pas être valide avec des données partielles."
