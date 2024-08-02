from data_access_layer.basic_db_functions import *
import requests
import os
import pytest

values_to_del = []

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Code to run before all tests
    print("\nSetup before all tests")
    yield
    # Code to run after all tests
    print("\nTeardown after all tests")
    # Delete the number from the database
    delete_number_from_db(number=values_to_del[0]) # make dynamic later
    values_to_del.pop(0)
    
def test_mongo_random_store_endpoint():
    server_url = os.getenv("SERVER_URL")
    assert server_url is not None
    response = requests.get(f"{server_url}/db/test")
    assert response.status_code == 200
    # Fetch the stored number from the response
    response = response.json()
    assert isinstance(response["stored_number"],int)
    stored_number = response["stored_number"]
    # Make sure the number is stored in the database
    check_result = check_exists_in_db(number=stored_number)
    assert isinstance(check_result,dict)
    assert "_id" in check_result
    # add the value to delete later as a part of cleanup
    values_to_del.append(stored_number)

def test_check_exists_in_db():
    assert check_exists_in_db(number = -1) is None # impossible because rand num gens nums from 1-1000
