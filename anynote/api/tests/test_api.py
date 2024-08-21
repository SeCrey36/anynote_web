from django.contrib.auth.models import User


def test_baked_model(db, user):
    """Test backed user model."""
    assert isinstance(user, User)

# def test_retrieve_account(api_client: APIClient):
#     response = api_client.get(f"/api/account/")
#     assert response.status_code == 200
