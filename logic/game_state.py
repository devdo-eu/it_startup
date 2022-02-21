from typing import Tuple

class GameState:
    def __init__(self):
        self.players = []
        self.deck = []
        self.active_player_id = 0
        self.finish_project_at = 32

    def ready(self) -> bool:
        return len(self.players) > 1 and len(self.deck) >= 32

    def game_finished(self) -> Tuple[bool, int, int]:
        finished = False
        winner_id = 0
        high_score = 0
        for player_id, player in enumerate(self.players):
            if player.project_points >= self.finish_project_at and player.project_points > high_score:
                high_score = player.project_points
                finished = True
                winner_id = player_id
        return finished, winner_id, high_score

