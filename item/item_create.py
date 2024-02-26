
import requests


def test_post_item():
    url = "https://test-bees.herokuapp.com/items.json"
    item_data = {
        "name": "Item Test",
        "height": 1.0,  # Replace with actual height
        "width": 1.0,  # Replace with actual width
        "weight": 1.0  # Replace with actual weight
    }
    response = requests.post(url, json=item_data)
    assert response.status_code == 201
    return response.json()
