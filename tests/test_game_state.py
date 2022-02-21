import pytest

from logic.game_state import GameState
from logic.player import Player

@pytest.fixture
def gs():
    gs = GameState()
    return gs

def test_sanity_check(gs):
    assert gs

def test_game_state_ready(gs):
    assert not gs.ready()

    gs.players = [0, 1]
    gs.deck = 32*[9]
    assert gs.ready()

def test_game_state_game_finished(gs):
    # GIVEN & WHEN
    finished, _, _ = gs.game_finished()

    # THEN
    assert not finished

    # GIVEN
    player_0, player_1 = Player(), Player()
    player_0.project_points = 50
    player_1.project_points = 25
    gs.players = [player_0, player_1]

    # WHEN
    finished, winner_id, high_score = gs.game_finished()

    # THEN
    assert finished
    assert winner_id == 0
    assert high_score == 50

    # GIVEN
    player_0.project_points = 50
    player_1.project_points = 60

    # WHEN
    finished, winner_id, high_score = gs.game_finished()

    # THEN
    assert finished
    assert winner_id == 1
    assert high_score == 60


