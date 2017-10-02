from unittest.mock import patch
import pytest
from unittest.test.testmock.testmock import MagicMock


@pytest.fixture()
def api():
    from nhl_stats.api.api import API
    api = API()
    return api


@patch('nhl_stats.api.api.requests.get')
def test_get_teams(mock_response, api):
    mock_response.return_value = MagicMock(response_code=200, text='{json}')

    teams_response = api.get_teams()

    assert 200 == teams_response.response_code
    assert '{json}' == teams_response.text

