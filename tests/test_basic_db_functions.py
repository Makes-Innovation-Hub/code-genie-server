from fastapi.testclient import TestClient
from data_access_layer.basic_db_functions import *
from server import app
import re

client = TestClient(app)

def test_test_store_in_db():
    response = client.get('/test/')
    assert response.status_code == 200
    # Fetch the stored number from the response
    stored_number = int(response.json().split()[0])
    # Make sure the number is stored in the database
    assert check_exists_in_db(number=stored_number)
    # Delete the number from the database
    delete_number_from_db(number=stored_number)
