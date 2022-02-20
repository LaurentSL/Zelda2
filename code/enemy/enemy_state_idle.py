from code.enemy.enemy_state import EnemyState


class EnemyStateIdle(EnemyState):

    def __init__(self, enemy):
        super().__init__(enemy, "idle")
