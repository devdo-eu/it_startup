from logic.actions.action import Action
from logic.enums.action_type import ActionType
from logic.game_state import GameState

class DiscardSelectedCard(Action):
    def __init__(self):
        Action.__init__(self)
        self.action_type = ActionType.END_TURN

    def do_action(self, gs: GameState):
        player = gs.players[gs.active_player_id]
        correct = len(player.hand) == 0
        card_id = -1

        stream = ''
        for card_id, card_name in enumerate(player.hand):
            stream += 'id: ' + str(card_id) + ' -> ' + card_name + '\n'

        while not correct:
            player.output(stream)
            card_id = player.input("Choose Card ID to Discard: ")
            try:
                card_id = int(card_id)
            except ValueError as e:
                player.output(str(e))
                continue
            correct = card_id <= len(player.hand)
            if not correct:
                player.output(f"No Such Card ID as {card_id}...")
        if len(player.hand) > 0:
            player.output(f"Card {player.hand[card_id]} has been discarded.")
            player.hand.remove(player.hand[card_id])
