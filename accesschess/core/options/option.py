"""
Individual options
Includes name, value, type, etc.
Metadata is option-specific data. For example min/max.
"""


class Option:
    def __init__(self, optionType, name, value, metadata):
        self.type = optionType
        self.name = name
        self.value = value
        self.metadata = metadata
