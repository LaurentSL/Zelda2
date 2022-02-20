from code.player.player_state import PlayerState


class PlayerStateIdle(PlayerState):

    def __init__(self, player):
        super().__init__(player, "idle")
