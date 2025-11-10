class StatisticsService:
    def __init__(self, player_reader):
        # player_reader on ulkopuolelta annettu PlayerReader-olio
        self._players = player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player
        return None

    def team(self, team_name):
        return [player for player in self._players if player.team == team_name]

    def top(self, how_many):
        sorted_players = sorted(self._players, reverse=True, key=lambda p: p.points)
        return sorted_players[:how_many]
