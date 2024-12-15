import pytest
from unittest.mock import patch, MagicMock
from backend.etl.etl import run_etl

@patch('backend.etl.etl.connect_to_db')
@patch('backend.etl.etl.extract_nyc_payroll_data')
@patch('backend.etl.etl.transform_data')
@patch('backend.etl.etl.load_data')
def test_run_etl(mock_load_data, mock_transform_data, mock_extract_data, mock_connect_db):
    mock_conn = MagicMock()
    mock_connect_db.return_value = mock_conn
    mock_extract_data.return_value = [{'EmployeeID': '123'}]
    mock_transform_data.return_value = [{'employee_id': '123'}]

    run_etl()

    mock_connect_db.assert_called_once()
    mock_extract_data.assert_called_once()
    mock_transform_data.assert_called_once_with([{'EmployeeID': '123'}])
    mock_load_data.assert_called_once_with(mock_conn, [{'employee_id': '123'}])
    mock_conn.close.assert_called_once()
