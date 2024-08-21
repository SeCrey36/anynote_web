from rest_framework.test import APIClient

import pytest


@pytest.fixture
def api_client():
    """Return API client from rest-framework.

    Allows to send requests to the api endpoints in tests.
    """
    return APIClient()
