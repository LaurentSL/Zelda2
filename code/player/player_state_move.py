from code.player.player_state import PlayerState


class PlayerStateMove(PlayerState):

    def __init__(self, player):
        super().__init__(player, "move")
