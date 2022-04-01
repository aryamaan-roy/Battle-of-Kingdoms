class building:
    def __init__(self, row, col):
        self.row = row
        self.col = col

structure_max_health = 100

class TownHall(building):
    def __init__(self, row, col):
        super().__init__(row,col)
        self.health = structure_max_health


class hut(building):
    def __init__(self, id, row, col):
        super().__init__(row,col)
        self.health = structure_max_health
        self.id = id


class wall(building):
    def __init__(self, id, row, col):
        super().__init__(row,col)
        self.id = id
        self.health = structure_max_health

class cannon(building):
    def __init__(self, id, row, col, c_range, damage):
        super().__init__(row,col)
        self.health = structure_max_health
        self.id = id
        self.c_range = c_range
        self.damage = damage
        self.is_attack = 0

