

class URLBuilder:

    def __init__(self):
        self.base_url = 'http://statsapi.web.nhl.com/api/v1/'

    def build_teams_url(self) -> str:
        teams_endpoint = 'teams'
        return '%s%s' % (self.base_url, teams_endpoint)
