import pytest
from app.backend.utils.db_utils import get_connection

def test_get_connection(db_connection):
    assert db_connection is not None
