import requests
import pytest


def test_post_inventory():
    url = "https://test-bees.herokuapp.com/inventories.json"

    response = requests.get(url)
    print(response.json())