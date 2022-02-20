from code.components.movement_component import MovementComponent
from code.player.player_state import PlayerState


class PlayerStateMove(PlayerState):

    def __init__(self, player):
        super().__init__(player, "move")
        self.movement_component = MovementComponent(self.player.obstacle_sprites,
                                                    self.player.animation_component,
                                                    self.player.animation_component.collision_box,
                                                    self.player.stats.speed)

    def update(self):
        x = self.player.direction_wanted.x
        y = self.player.direction_wanted.y
        self.movement_component.set_normalized_direction(x, y)
        self.movement_component.update()
        self.player.direction_name = self.movement_component.get_direction_name()

    def stop(self):
        self.movement_component.stop()

