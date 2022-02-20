from code.components.movement_component import MovementComponent
from code.enemy.enemy_state import EnemyState


class EnemyStateMove(EnemyState):

    def __init__(self, enemy):
        super().__init__(enemy, "move")
        self._movement_component = MovementComponent(self.enemy.obstacle_sprites,
                                                     self.enemy.animation_component,
                                                     self.enemy.animation_component.collision_box,
                                                     self.enemy.stats.speed)

    def move(self):
        direction_to_player = self.enemy.get_direction_to_player()
        self._movement_component.move_to(direction_to_player)
        self.enemy.animation_component.position = self._movement_component.position

    def update(self):
        self.move()
