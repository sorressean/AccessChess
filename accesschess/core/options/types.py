"""
Option types declare the type of game engine options.
"""

import enum


class OptionType(enum.Enum):
    String = 1
    Number = 2
    Boolean = 3
