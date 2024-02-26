import uuid

import requests


def test_get_items():
    url = "https://test-bees.herokuapp.com/items.json"
    response = requests.get(url)
    assert response.status_code == 200
    items = response.json()
    for item in items:
        assert 'id' in item
        assert 'name' in item
        assert 'height' in item
        assert 'width' in item
        assert 'weight' in item
        assert 'created_at' in item
        assert 'updated_at' in item
        assert 'url' in item
    return items
