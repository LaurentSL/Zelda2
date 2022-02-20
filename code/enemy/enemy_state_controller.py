from code.enemy.enemy_state_idle import EnemyStateIdle
from code.enemy.enemy_state_move import EnemyStateMove
from code.enemy.enemy_state_can_attack import EnemyStateCanAttack
from code.enemy.enemy_state_attack import EnemyStateAttack


class EnemyStateController:

    def __init__(self, enemy):
        self._enemy = enemy
        self._state = EnemyStateIdle(self._enemy)
        self._state_exit = {
            EnemyStateIdle: self._state_idle_exit,
            EnemyStateMove: self._state_move_exit,
            EnemyStateCanAttack: self._state_can_attack_exit,
            EnemyStateAttack: self._state_attack_exit
        }

    def update(self):
        self._state.update()
        class_type = type(self._state)
        self._state_exit[class_type]()

    def get_status_name(self):
        return self._state.get_status_name()

    def is_attacking(self):
        return isinstance(self._state, EnemyStateAttack)

    def _change_state(self, state):
        self._state = state(self._enemy)

    def _state_idle_exit(self):
        if self._enemy.is_in_attack_radius():
            self._change_state(EnemyStateCanAttack)
        elif self._enemy.is_in_notice_radius():
            self._change_state(EnemyStateMove)

    def _state_move_exit(self):
        if self._enemy.is_in_attack_radius():
            self._change_state(EnemyStateCanAttack)
        elif not self._enemy.is_in_notice_radius():
            self._change_state(EnemyStateIdle)

    def _state_can_attack_exit(self):
        if not self._enemy.is_in_attack_radius():
            self._change_state(EnemyStateMove)
        elif not self._enemy.is_attacking():
            self._change_state(EnemyStateAttack)

    def _state_attack_exit(self):
        if self._enemy.animation_component.is_ending:
            self._change_state(EnemyStateIdle)
