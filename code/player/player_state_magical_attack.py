from code.player.player_state import PlayerState


class PlayerStateMagicalAttack(PlayerState):

    def __init__(self, player):
        super().__init__(player, "attack")
        self.player.magic_component.create_attack()
