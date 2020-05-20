from dataclasses import dataclass


@dataclass
class Bidder:

    @property
    def adjustment(self):
        return self._adjustment

    @adjustment.setter
    def adjustment(self, value):
        self._adjustment = value

    @property
    def name(self):
        return self._name

    def __init__(self, name=None, adjustment=None):
        self._name = name
        self._adjustment = adjustment

