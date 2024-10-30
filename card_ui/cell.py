"""
The Cell class will hold cell data and is responsible for formatting itself based on its
attributes and inputs.
"""

import textwrap
from typing import Self


class Cell:
    """
    The Cell class will hold cell data and is responsible for formatting itself based
    on its attributes and inputs.
    """

    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.formatted_data = []
        self.__x_size = 0  # Absolute width of cell
        self.__y_size = 0  # Absolute height of cell
        self.__x_pad = 0  # Padding between text and cell left/right edges
        self.__x_align = "left"

    # TODO: Set up controlled access points to ensure order is always followed when adjusting some attributes
    # TODO `def process_newline_chars` in data = new line in cell

    @property
    def x_size(self):
        """Returns the horizontal/x dimension of cell"""
        return self.__x_size

    @property
    def y_size(self):
        """Returns the vertical/y dimension of cell"""
        return len(self.formatted_data)

    def __wrap_text(self):
        """Wraps text into a list, splitting into multiple lines if needed"""
        if self.__x_size < len(self.raw_data):
            self.formatted_data = textwrap.wrap(
                self.raw_data, self.__x_size - self.__x_pad
            )
        else:
            self.formatted_data = [self.raw_data]

        # Always recalc y_size after wrapping
        self.__y_size = len(self.formatted_data)

    def __x_align_data(self):
        """
        Aligns and fills whitespace to create a formatted string
        Note: Requires self.wrap_text() and cannot be called directly.
        """
        # Align to available width
        data_x_size = self.__x_size - (self.__x_pad * 2)
        for i, data in enumerate(self.formatted_data):
            if self.__x_align == "left":
                self.formatted_data[i] = f"{data}".ljust(data_x_size)
            elif self.__x_align == "center":
                self.formatted_data[i] = f"{data}".center(data_x_size)
            elif self.__x_align == "right":
                self.formatted_data[i] = f"{data}".rjust(data_x_size)

    def __x_pad_cell(self):
        """Pads the left/right edges of the cell, regardless of alignment type"""
        # TODO: check for odd-number input handling
        for i, data in enumerate(self.formatted_data):
            if self.__x_pad > 0:
                self.formatted_data[i] = f"{data}".center(self.__x_size)

    def resize_x(self, x_size: int = 0, x_align=None, x_pad=None) -> Self:
        """Triggers Cell reprocessing to fit the new x_size"""
        self.__x_size = x_size if x_size >= 0 else self.__x_size
        self.__x_pad = x_pad if x_pad else self.__x_pad
        self.__x_align = x_align if x_align else self.__x_align
        self.__wrap_text()
        self.__x_align_data()
        self.__x_pad_cell()
        return self

    def resize_y(self, y_size: int) -> Self:
        """Add/removes list elements in formatted data to meet y_size requirements"""
        if y_size >= 0:
            # Assign y, trim formatted_data if too long
            self.__y_size = y_size
            self.formatted_data = self.formatted_data[: self.__y_size]
            # If too short, add filled whitespace strings to list
            while self.__y_size > len(self.formatted_data):
                self.formatted_data.append(" " * self.__x_size)
        return self

    def __str__(self) -> str:
        return "\n".join(self.formatted_data)


"test data           "
