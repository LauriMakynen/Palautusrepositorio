import pytest
from player import Player
from statistics_service import StatisticsService

# Luodaan "fake" PlayerReader, jotta ei tarvitse ladata oikeaa URL:ia käyttäen
class FakePlayerReader:
    def get_players(self):
        return [
            Player("Wayne Gretzky", "EDM", 50, 80),
            Player("Mario Lemieux", "PIT", 40, 70),
            Player("Sidney Crosby", "PIT", 35, 60),
            Player("Claude Giroux", "PHI", 30, 55),
        ]

@pytest.fixture
def stats_service():
    reader = FakePlayerReader()
    return StatisticsService(reader)

def test_search(stats_service):
    player = stats_service.search("Wayne Gretzky")
    assert player is not None
    assert player.name == "Wayne Gretzky"
    assert player.team == "EDM"

    # Etsitään pelaajaa, jota ei ole
    assert stats_service.search("Nonexistent Player") is None

def test_team(stats_service):
    pit_players = stats_service.team("PIT")
    assert len(pit_players) == 2
    assert all(player.team == "PIT" for player in pit_players)

    phi_players = stats_service.team("PHI")
    assert len(phi_players) == 1
    assert phi_players[0].name == "Claude Giroux"

def test_top(stats_service):
    top_players = stats_service.top(2)
    assert len(top_players) == 2
    # Top-pisteiden tarkistus (points = goals + assists)
    points = [p.points for p in top_players]
    assert points == sorted(points, reverse=True)
