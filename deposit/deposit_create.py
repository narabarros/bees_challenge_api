import requests
import pytest


def test_post_deposit():
    url = "https://test-bees.herokuapp.com/deposits.json"

    deposit_data = {
        "name": "test",
        "address": "Rua Teste, 123",
        "city": "Cidade Teste",
        "state": "Estado Teste",
        "zipcode": "12345-678"
    }

    response = requests.post(url, json=deposit_data)
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    returned_deposit = response.json()
    assert returned_deposit["name"] == deposit_data["name"]
    assert returned_deposit["address"] == deposit_data["address"]
    assert returned_deposit["city"] == deposit_data["city"]
    assert returned_deposit["state"] == deposit_data["state"]
    assert returned_deposit["zipcode"] == deposit_data["zipcode"]
    return returned_deposit
