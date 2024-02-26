import requests
import pytest


def test_get_deposits():
    url = "https://test-bees.herokuapp.com/deposits.json"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    deposits = response.json()
    for deposit in deposits:
        validate_deposit_struct(deposit)

    return deposits


def validate_deposit_struct(deposit_data):
    assert 'id' in deposit_data
    assert 'name' in deposit_data
    assert 'address' in deposit_data
    assert 'city' in deposit_data
    assert 'state' in deposit_data
    assert 'zipcode' in deposit_data
    assert 'created_at' in deposit_data
    assert 'updated_at' in deposit_data
    assert 'items' in deposit_data
    assert 'url' in deposit_data
