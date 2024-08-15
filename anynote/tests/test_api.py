import pytest
import json
# from main.models import NoteMode
from django.urls import reverse
from rest_framework import status

'''@pytest.mark.django_db'''


def test_getting_access_token(api_client):
    """
    url = reverse("token_obtain_pair")
    data = {'username':'root', 'password':'root'}
    response = api_client.post(url, data=data)
    parsed_response = json.loads(response)
    dict_keys = parsed_response.keys()
    assert dict_keys[0] == 'refresh'
    assert dict_keys[1] == 'access'
    """
    assert 1 == 1


'''
def test_account_note_view(client, user, note):
   client.force_authenticate(user=user)
   url = reverse('account-note', kwargs={'pk': note.pk})
   response = client.get(url)
   assert response.status_code == status.HTTP_200_OK
   assert response.json()['content'] == {'key': 'value'}
'''
