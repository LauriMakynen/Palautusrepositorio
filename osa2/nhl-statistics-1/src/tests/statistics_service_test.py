import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.team, "EDM")

    def test_search_returns_none_if_not_found(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        team_players = self.stats.team("EDM")
        self.assertEqual(len(team_players), 3)
        self.assertTrue(all(p.team == "EDM" for p in team_players))

    def test_top_returns_correct_number_of_players(self):
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)

    def test_top_players_are_sorted_by_points(self):
        top_players = self.stats.top(3)
        points = [p.points for p in top_players]
        self.assertEqual(points, sorted(points, reverse=True))

    def test_top_zero_returns_empty_list(self):
        top_players = self.stats.top(0)
        self.assertEqual(top_players, [])