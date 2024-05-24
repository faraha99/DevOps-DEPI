# tests/test_app.py
import sys
import os
import pytest
import json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home route"""
    response = client.get('/')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'current_time' in data
    assert 'time_zone' in data
    assert data['time_zone'] == 'Africa/Cairo'
    assert 'weather' in data
    assert 'description' in data['weather']
    assert 'temperature' in data['weather']

def test_time_format(client):
    """Test the time format"""
    response = client.get('/')
    data = json.loads(response.data)
    time_str = data['current_time']
    # Check if time string contains AM or PM
    assert 'AM' in time_str or 'PM' in time_str
