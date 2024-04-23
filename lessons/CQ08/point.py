"""Create a Point Class."""

from __future__ import annotations

__author__ = "730553436"


class Point:
    """Class Point that is used."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Create the general Point Class."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Change values for the floats."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Returns new points."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point