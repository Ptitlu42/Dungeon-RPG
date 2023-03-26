class Case:

    def __init__(self, pos_x, pos_y, sprite, deco, info, occuped_by) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.sprite = sprite
        self.deco = deco
        self.info = info
        self.occuped_by = occuped_by

    def __str__(self):
        t = f"pos x : {self.pos_x} / pos_y : {self.pos_y}"
        return t

    def __repr__(self):
        t = f"pos x : {self.pos_x} / pos_y : {self.pos_y}"
        return t


