from enum import Enum


class Commands(Enum):
    """
    Commands received by the service.
    Command "name" received from the engine is always excepted to be in all lower-case letters.
    """
    implement_treatment_result = {"name": "implement_treatment_result", }

    def __init__(self, value):
        if "name" not in value:
            raise ValueError("Key 'name' needs to be provided")

    @property
    def name(self):
        return self.value["name"]

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)
