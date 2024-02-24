import requests
import pytest


def test_delete_inventory():
    url = "https://test-bees.herokuapp.com/inventories/10.json"

    response = requests.delete(url)
