import pytest


@pytest.fixture()
def url_builder():
    from nhl_stats.api.url_builder import URLBuilder
    url_builder = URLBuilder()
    return url_builder


def test_build_teams_url(url_builder):
    expected_teams_url = 'http://statsapi.web.nhl.com/api/v1/teams'

    teams_url = url_builder.build_teams_url()

    assert expected_teams_url == teams_url

