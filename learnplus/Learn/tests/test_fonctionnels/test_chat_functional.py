import pytest
@pytest.mark.django_db
def test_private_chat_functionality(client, django_user_model):
    user1 = django_user_model.objects.create_user(username="etudiant1", password="1234")
    user2 = django_user_model.objects.create_user(username="etudiant2", password="1234")
    client.login(username="etudiant1", password="1234")
    response = client.post(reverse("private_chat", args=[user2.id]), {"message": "Bonjour"})
    assert response.status_code == 200
    assert b"Bonjour" in response.content
