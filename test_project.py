import csv
import pytest
from unittest.mock import patch, mock_open
from project import validate_username, validate_password, create_account


# Test validate_username()
@patch('project.LogIn.landing', return_value='JohnDoe')  # Replace with correct path
@patch('builtins.open', new_callable=mock_open, read_data='name,password\nJohnDoe,pass123\nJaneDoe,pass456')
def test_validate_username(mock_open, mock_landing):
    assert validate_username() == 'JohnDoe'

@patch('project.LogIn.landing', return_value='Bob')  # Replace with correct path
@patch('builtins.open', new_callable=mock_open, read_data='name,password\nBob,pass123')
def test_validate_username(mock_open, mock_landing):
    assert validate_username() == 'Bob'


# Test validate_password()
@patch('project.LogIn.existing_account', return_value='123apples')  # Replace with correct path
@patch('builtins.open', new_callable=mock_open, read_data='name,password\nJohnDoe,123apples')
def test_validate_password(mock_open, mock_landing):
    result = validate_password('JohnDoe')
    assert result == True

@patch('project.LogIn.existing_account', return_value='bananas')  # Replace with correct path
@patch('builtins.open', new_callable=mock_open, read_data='name,password\ntomato,123apples')
def test_validate_password(mock_open, mock_landing):
    result = validate_password('jane')
    assert result == False


# Test create_account
@patch('project.LogIn.new_account', return_value='2')  # Replace with correct path
def test_create_account(mock_open):
    result = create_account()
    assert result == True

@patch('project.LogIn.new_account', return_value='3')  # Replace with correct path
def test_create_account(mock_open):
    with pytest.raises(SystemExit):
        assert create_account()


