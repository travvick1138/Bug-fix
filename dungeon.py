from random import randint

class Dungeon:

    def __init__(self):

        self.dungeon_size = 0 # Can be range from (i-2) - i rooms
        self.dungeon_rooms = [] # Should be an embedded list of rooms
        self.dungeon_weapons = {}
        self.dungeon_monsters = {}

        """Dungeon Layout:

            [
                [r_11,r_12,r_13],
                [r_21,r_22]
                [r_31,r_32,r_33],
                [r_41],
                [r_51],...............r5100]
            ]

        """

    def generate_dungeon():
        pass
        # define dungeon size
        # self.dungeon_size = randint(3,12)
        # rooms_to_create = self.dungeon_size
        # x = 1
        # y = 1
        #
        # # Create
        # while rooms_to_create > 0:
        #     if x == 1 and y == 1:
        #         create_start_room():
        #     else:
        #         build_direction = randint(0,1)
        #         if build_direction:
        #             # build right
        #             x += 1
        #             create_room(x,y)
        #         else:
        #             # build down
        #             y += 1
        #             x = 1
        #             create_room(x,y)
        #
        #     rooms_to_create -= 1



    def load_dungeon(json):
        pass
