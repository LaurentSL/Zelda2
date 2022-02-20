class PlayerState:

    def __init__(self, player, status_name):
        self.player = player
        self.status_name = status_name

    def change_state(self, state):
        self.player._state = state(self.player)

    def update(self):
        pass

    def move(self):
        pass

    def attack(self):
        pass

    def get_status_name(self):
        return self.status_name

