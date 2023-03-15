import Mob
class smallMob(Mob.Mob):

    def __init__(self, specialAttack, name, vitality, strength, level) -> None:
        super().__init__(name, vitality, strength, level)
        self.specialAttack = specialAttack
        