import pytest
from fastapi import HTTPException
from data_access_layer.users_challenge_db_functions import store_username, check_and_delete_username

def test_store_username_success():
    username = 'test_username ' * 5
    response = store_username(username=username)
    assert response['username'] == username
    assert response['available'] is True
    assert check_and_delete_username(username=username)

def test_store_username_failure():
    username = 'test_username ' * 5
    store_username(username=username)

    with pytest.raises(HTTPException) as info:
        store_username(username=username)

    assert info.value.status_code == 409
    assert info.value.detail == 'Username already exists'
    check_and_delete_username(username=username)
