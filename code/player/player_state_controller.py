from code.player.player_state_idle import PlayerStateIdle
from code.player.player_state_move import PlayerStateMove
from code.player.player_state_attack import PlayerStateAttack


class PlayerStateController:

    def __init__(self, player):
        self._player = player
        self._state = PlayerStateIdle(self._player)
        self._state_exit = {
            PlayerStateIdle: self._state_idle_exit,
            PlayerStateMove: self._state_move_exit,
            PlayerStateAttack: self._state_attack_exit
        }

    def update(self):
        self._state.update()
        class_type = type(self._state)
        self._state_exit[class_type]()

    def get_status_name(self):
        return self._state.get_status_name()

    def is_attacking(self):
        return isinstance(self._state, PlayerStateAttack)

    def _change_state(self, state):
        self._state = state(self._player)

    def _state_idle_exit(self):
        if self._player.is_in_attack_radius():
            self._change_state(PlayerStateCanAttack)
        elif self._player.is_in_notice_radius():
            self._change_state(PlayerStateMove)

    def _state_move_exit(self):
        if self._player.is_in_attack_radius():
            self._change_state(PlayerStateCanAttack)
        elif not self._player.is_in_notice_radius():
            self._change_state(PlayerStateIdle)

    def _state_can_attack_exit(self):
        if not self._player.is_in_attack_radius():
            self._change_state(PlayerStateMove)
        elif not self._player.is_attacking():
            self._change_state(PlayerStateAttack)

    def _state_attack_exit(self):
        if self._player.animation_component.is_ending:
            self._change_state(PlayerStateIdle)
