import pytest
@pytest.mark.django_db
def test_student_can_participate_in_quiz(client, django_user_model):
    user = django_user_model.objects.create_user(username="etudiant1", password="1234")
    client.login(username="etudiant1", password="1234")
    response = client.get(reverse("quiz_participation", args=[1]))
    assert response.status_code == 200
    assert b"Commencer le Quiz" in response.content
