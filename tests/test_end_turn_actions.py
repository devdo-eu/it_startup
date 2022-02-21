import pytest

from logic.game_state import GameState
from logic.player import Player
from logic.actions.end_turn_actions import DiscardSelectedCard

@pytest.fixture
def gs():
    return GameState()

@pytest.fixture
def player():
    return Player()

def fake_input_prep(fake_input):
    index = -1
    def inner(text):
        nonlocal index
        print(text)
        index = index + 1
        return fake_input[index]
    return inner

class TestDiscardSelectedCard:
    action = DiscardSelectedCard()

    def test_player_has_cards_correct_second_input(self, gs, player):
        # GIVEN
        player.hand = ['a', 'b', 'c']
        player.input = fake_input_prep(['8','1'])
        gs.players = [player]

        # WHEN
        self.action.do_action(gs)

        # THEN
        assert len(player.hand) == 2
        assert player.hand[0] == 'a'
        assert player.hand[1] == 'c'

    def test_player_has_0_cards(self, gs, player):
        # GIVEN
        player.hand = []
        player.input = fake_input_prep([])
        gs.players = [player]

        # WHEN
        self.action.do_action(gs)

        # THEN
        assert len(player.hand) == 0

    def test_incorrect_input_then_correct_input(self, gs, player):
        # GIVEN
        player.hand = ['a', 'b', 'c']
        player.input = fake_input_prep(['nonsense', '2'])
        gs.players = [player]

        # WHEN
        self.action.do_action(gs)

        # THEN
        assert len(player.hand) == 2
        assert player.hand[0] == 'a'
        assert player.hand[1] == 'b'