"""Base class for game entities.
Characters are mostly properties set by the user but also require
state persistence such as things acquired."""

from abc import ABC, abstractmethod


class AbstractBaseEntity(ABC):
    """Base entity class, implements common characteristics and state storage."""

    def __init__(self):
        """Set up the character, base properties, numeric attributes and storage."""
        self.name = ""
        self.description = ""
        self.attributes = {
            'strength': 0,
            'skill': 0,
            'health': 0
        }
        self.stuff = []
