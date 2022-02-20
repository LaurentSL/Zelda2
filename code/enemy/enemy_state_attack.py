from code.enemy.enemy_state import EnemyState
from code.timer import Timer


class EnemyStateAttack(EnemyState):

    def __init__(self, enemy):
        super().__init__(enemy, "attack")
        self._timer_attack = Timer(1000)
        self._attack()

    def update(self):
        self._timers_update()

    def _attack(self):
        self._timer_attack.launch()

    def _timers_update(self):
        self._timer_attack.update()

    def _is_attacking(self):
        return self._timer_attack.is_running
