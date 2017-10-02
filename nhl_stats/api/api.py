import requests
from nhl_stats.api.url_builder import URLBuilder


class API:

    def __init__(self):
        self.url_builder = URLBuilder()

    def get_teams(self):
        teams = requests.get(self.url_builder.build_teams_url())
        return teams
