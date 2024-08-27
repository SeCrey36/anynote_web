from django.contrib.auth.models import User

import pytest
from model_bakery import baker


@pytest.fixture
def user():
    """Fixture for baked User model."""
    return baker.make(User)


