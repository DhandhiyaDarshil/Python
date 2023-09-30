class Entity:
    def __init__(self, movement, health, speed) -> None:
        self.movement_allowed = movement
        self.health = health
        self.speed = speed

    def define(self) -> None:
        print(f'Movement: {self.movement_allowed}\nSpeed: {self.speed}\nHealth: {self.health}')


class Player(Entity):
    def __init__(self, movement, health, speed, name, attacking_speed, damage) -> None:
        super().__init__(movement, health, speed)
        self.name = name
        self.attacking_speed = attacking_speed
        self.damage = damage

    def define(self) -> None:
        print(f'Name: {self.name}\nAttacking Speed: {self.attacking_speed}\nDamage: {self.damage}', end='')
        super().define()


p1 = Player(name='player1', movement=True, speed=10, attacking_speed=10, health=200, damage=1)
