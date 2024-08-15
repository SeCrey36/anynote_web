import django
import pytest
from django.conf import settings
import django
import os
import sys
from dotenv import load_dotenv, find_dotenv

# from django.contrib.auth.models import User

# dotenv_path = find_dotenv(filename='.env', raise_error_if_not_found=True)
load_dotenv()
print(sys.path)

print(f"INSTALLED_APPS: {settings.INSTALLED_APPS}")


@pytest.fixture(autouse=True)
def setup_django(request):
    django.setup()


"""
@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password')

@pytest.fixture
def note(user):
    return NoteModel.objects.create(user=user, content={'key': 'value'}, hash='hash')
"""


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
