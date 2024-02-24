import requests
import pytest


def test_post_inventory():
    url = "https://test-bees.herokuapp.com/inventories.json"

    inventory_data = {
        "item_id": 14,
        "deposit_id": 47,
        "item_count": 1024
    }
    response = requests.post(url, json=inventory_data)
    print(response.json())

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    returned_inventory = response.json()

    assert returned_inventory["item_id"] == inventory_data["item_id"]
    assert returned_inventory["deposit_id"] == inventory_data["deposit_id"]
    assert returned_inventory["item_count"] == inventory_data["item_count"]