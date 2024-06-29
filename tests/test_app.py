import sys
import os
import pytest

# Insert the parent directory into the sys.path to import the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Choose a Country' in rv.data

def test_post_country(client):
    rv = client.post('/', data={'country': 'Egypt'})
    assert rv.status_code == 200
    assert b'Time and Weather in Cairo, Egypt' in rv.data

def test_invalid_country(client):
    rv = client.post('/', data={'country': 'InvalidCountry'})
    assert rv.status_code == 200
    assert b'Time and Weather in' not in rv.data
