import pytest
@pytest.mark.django_db
def test_quiz_submission(client, django_user_model):
    user = django_user_model.objects.create_user(username="etudiant1", password="1234")
    client.login(username="etudiant1", password="1234")
    response = client.post(reverse("quiz_submit", args=[1]), {"answers": {"q1": "A", "q2": "B"}})
    assert response.status_code == 200
    assert b"Votre score" in response.content
