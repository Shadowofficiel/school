import pytest
from django.urls import reverse
from quiz.models import Quiz, Question, Reponse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_quiz_creation_flow(client):
    # Créer un utilisateur et se connecter
    user = User.objects.create_user(username="etudiant1", password="1234")
    client.login(username="etudiant1", password="1234")
    
    # Créer un quiz via la vue
    quiz_data = {"title": "Integration Quiz", "description": "Test d'intégration du quiz"}
    response = client.post(reverse('quiz_create'), data=quiz_data)
    assert response.status_code == 302  # Redirection après création
    quiz = Quiz.objects.get(title="Integration Quiz")
    assert quiz.description == "Test d'intégration du quiz"
    
    # Ajouter une question au quiz
    question_data = {"quiz": quiz.id, "text": "Quelle est la capitale de la France ?"}
    response = client.post(reverse('question_create', args=[quiz.id]), data=question_data)
    assert response.status_code == 302  # Redirection après création
    question = Question.objects.get(quiz=quiz, text="Quelle est la capitale de la France ?")
    assert question.quiz == quiz
    
    # Ajouter une réponse à la question
    reponse_data = {"question": question.id, "text": "Paris", "is_correct": True}
    response = client.post(reverse('reponse_create', args=[question.id]), data=reponse_data)
    assert response.status_code == 302  # Redirection après création
    reponse = Reponse.objects.get(question=question, text="Paris")
    assert reponse.is_correct is True

@pytest.mark.django_db
def test_quiz_update_flow(client):
    # Créer un quiz initialement
    quiz = Quiz.objects.create(title="Old Title", description="Old Description")
    
    # Modifier les informations du quiz
    data = {"title": "Updated Title", "description": "Updated Description"}
    response = client.post(reverse('quiz_update', args=[quiz.id]), data=data)
    assert response.status_code == 302  # Redirection après mise à jour
    quiz.refresh_from_db()
    assert quiz.title == "Updated Title"
    assert quiz.description == "Updated Description"

@pytest.mark.django_db
def test_quiz_deletion_flow(client):
    # Créer un quiz
    quiz = Quiz.objects.create(title="To Be Deleted", description="A supprimer")
    
    # Supprimer le quiz
    response = client.post(reverse('quiz_delete', args=[quiz.id]))
    assert response.status_code == 302  # Redirection après suppression
    assert not Quiz.objects.filter(id=quiz.id).exists()
