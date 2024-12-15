import sys
import os
import pytest

# Adjust the path for the tests
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

@pytest.fixture(scope='session')
def db_connection():
    from app.backend.utils.db_utils import get_connection
    return get_connection()
