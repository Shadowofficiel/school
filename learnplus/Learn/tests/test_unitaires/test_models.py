# test_models.py
import pytest
from quiz.models import Quiz, Question
from chat.models import Message, Salon

@pytest.mark.django_db
def test_quiz_creation():
    quiz = Quiz.objects.create(title="Test Quiz", description="A test quiz description.")
    assert quiz.title == "Test Quiz"
    assert str(quiz) == "Test Quiz"


@pytest.mark.django_db
def test_question_creation():
    quiz = Quiz.objects.create(title="Test Quiz", description="Test quiz description.")
    question = Question.objects.create(quiz=quiz, text="What is pytest?")
    assert question.quiz == quiz
    assert question.text == "What is pytest?"

from django.urls import reverse

@pytest.mark.django_db
def test_quiz_list_view(client):
    response = client.get(reverse('quiz_list'))
    assert response.status_code == 200
    assert b"Quizzes" in response.content

@pytest.mark.django_db
def test_quiz_detail_view(client):
    quiz = Quiz.objects.create(title="Test Quiz", description="Test description")
    response = client.get(reverse('quiz_detail', args=[quiz.id]))
    assert response.status_code == 200
    assert b"Test Quiz" in response.content

