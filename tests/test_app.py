import sys
import os
import pytest
from flask import Flask

# Add the parent directory to the sys.path to import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the app after adding it to sys.path
from app import app

# Mock API_KEY for testing
os.environ['API_KEY'] = 'mock_api_key_for_testing'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Choose a Country' in rv.data

def test_invalid_country(client):
    rv = client.post('/', data={'country': 'InvalidCountry'})
    assert rv.status_code == 200
    assert b'Time and Weather in' not in rv.data
