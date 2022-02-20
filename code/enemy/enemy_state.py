class EnemyState:

    def __init__(self, enemy, status_name):
        self.enemy = enemy
        self.status_name = status_name

    def move(self):
        pass

    def get_status_name(self):
        return self.status_name

    def update(self):
        pass
