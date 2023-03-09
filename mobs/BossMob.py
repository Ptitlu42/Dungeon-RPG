import Mob

class smallMob(Mob):

    def __init__(self, name, vitality, strength, level, specialAttack) -> None:
        super().__init__(self, name, vitality, strength, level)
        self.specialAttack = specialAttack
        