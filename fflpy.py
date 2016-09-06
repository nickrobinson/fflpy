import requests


class EspnFflClient:
    def __init__(self, league_id):
        self.leagueId = league_id
        self.ENDPOINT = 'http://games.espn.com/ffl/api/v2/'
        self.RAND = '00921504334023'

    def get_recent_activity(self, count=20):
        url = self.ENDPOINT + 'recentActivity?' + '?leagueId=' + str(self.leagueId) + '&count=' + str(
            count) + '&rand=' + self.RAND
        r = requests.get(url)
        return r.json()

    def get_player_info(self, player_id):
        url = self.ENDPOINT + 'playerInfo' + '?leagueId=' + str(self.leagueId) + '&playerId=' \
              + str(player_id) + '&include=gamesLog|news|projections|playerInfos' + '&rand=' + self.RAND
        r = requests.get(url)
        return r.json()


client = EspnFflClient(460537)
print(client.get_recent_activity(20))
print(client.get_player_info(18026))
