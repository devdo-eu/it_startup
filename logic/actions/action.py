from logic.enums.action_type import ActionType
from logic.game_state import GameState

class Action:
    def __init__(self):
        self.action_type = ActionType.NONE

    def do_action(self, gs: GameState):
        assert False