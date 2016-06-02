"""Ring class, inherits from GenericObject

>>> Ring = Ring('i am a ring')
>>> ring.description
'i am a ring'

>>> ring.i_am_a
'ring'

"""

from genericobject import GenericObject

"""

State:
    emoji: 💍
    ability: open locked doors

"""


class Ring(GenericObject):
    """Blueprint for a ring in the Dungeon of Doom!

    Extends GenericObject
    """

    def __init__(self, description):
        """Initialize"""
        super().__init__(description)
        self.i_am_a = 'ring'
        self.emoji = '💍'

    def __repr__(self):
        return """Ring(description={self.description}, i_am_a={self.i_am_a}, emoji={self.emoji}""".format(self=self)

if __name__ == '__main__':
    from doctest import testmod

    testmod()  # Run our unit tests when the script is run with the -v option