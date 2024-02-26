import requests
import pytest


def test_get_inventory():
    url = "https://test-bees.herokuapp.com/inventories.json"

    response = requests.get(url)
    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    inventories = response.json()
    for inventory in inventories:
        assert 'id' in inventory
        assert 'item_id' in inventory
        assert 'deposit_id' in inventory
        assert 'item_count' in inventory
        assert 'created_at' in inventory
        assert 'updated_at' in inventory
        assert 'url' in inventory

    return inventories
