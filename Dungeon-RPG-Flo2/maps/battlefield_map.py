class Battlefield:

    def __init__(self):
        # sprites path
        G = "/sprites/grass1.png"
        D = "/sprites/dirt.png"


        self.map_sprites = [[D, D, D, D, D, D, D, D, D, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, G, G, G, G, G, G, G, G, D],
                            [D, D, D, D, D, D, D, D, D, D]]

        self.map_deco = [[G, G, G, G, G, G, G, G, G, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, 0, 0, 0, 0, 0, 0, 0, 0, G],
                         [G, G, G, G, G, G, G, G, G, G]]
