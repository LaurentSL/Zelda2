from code.enemy.enemy_state import EnemyState


class EnemyStateCanAttack(EnemyState):

    def __init__(self, enemy):
        super().__init__(enemy, "can_attack")
