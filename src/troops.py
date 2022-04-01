class Troops:
    def __init__(self,row,col,damage,speed):
        self.row = row
        self.col = col
        self.damage = damage
        self.speed = speed
        
# max king health
max_king_health = 1000
class king(Troops):
    def __init__(self, row, col, damage,speed):
        super().__init__(row,col,damage,speed)
        self.health = max_king_health
    def heal_spell(self):
        self.health = self.health*1.5
        if self.health > max_king_health:
            self.health = max_king_health
    def rage_spell(self):
        self.speed = self.speed*2
        self.damage = self.damage*2

max_barbarian_health = 500
class barbarians(Troops):
    def __init__(self, row, col, damage, speed):
        super().__init__(row,col,damage,speed)
        self.health = max_barbarian_health
    def heal_spell(self):
        self.health = self.health*1.5
        if self.health > max_barbarian_health:
            self.health = max_barbarian_health
    def rage_spell(self):
        self.speed = self.speed*2
        self.damage = self.damage*2



