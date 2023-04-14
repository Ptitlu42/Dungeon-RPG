class Item:

    def __init__(self, id, equipable, name, emplacement, strength_mod, life_mod, speed_mod, const_mod, ap_mod, heal, range, ranged_damage) -> None:
        self.id = id
        self.equipable = equipable
        self.name = name
        self.emplacement = emplacement
        self.strength_mod = strength_mod
        self.life_mod = life_mod
        self.speed_mod = speed_mod
        self.const_mod = const_mod
        self.ap_mod = ap_mod
        self.heal = heal
        self.range = range
        self.ranged_damage = ranged_damage

    """def __repr__(self):
        print(self.name, self.strength_mod, self.life_mod)"""

    def get_item_id(self, id, item_list):
        n = len(item_list)
        for i in range(n):
            if item_list[i].id == id:
                return item_list[i]



