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
        self.x_size = 0  # Absolute width of cell
        self.y_size = 0  # Absolute height of cell
        self.x_pad = 0  # Padding between text and cell left/right edges
        self.x_align = "left"

    # TODO: Set up controlled access points to ensure order is always followed when adjusting some attributes
    # TODO `def process_newline_chars` in data = new line in cell

    def wrap_text(self) -> Self:
        """Wraps text into a list, splitting into multiple lines if needed"""
        # TODO: Max lines if y_size set?
        if self.x_size < len(self.raw_data):
            self.formatted_data = textwrap.wrap(self.raw_data, self.x_size - self.x_pad)
        else:
            self.formatted_data = [self.raw_data]
        return self

    def __x_align_data(self, x_align: str = None):
        """
        Aligns and fills whitespace to create a formatted string
        Note: Requires self.wrap_text() and cannot be called directly.
        """
        # Update internal attribute if needed
        self.x_align = x_align if x_align else self.x_align

        # Align to available width
        data_x_size = self.x_size - self.x_pad
        for i, data in enumerate(self.formatted_data):
            if self.x_align == "left":
                self.formatted_data[i] = f"{data}".ljust(data_x_size)
            elif self.x_align == "center":
                self.formatted_data[i] = f"{data}".center(data_x_size)
            elif self.x_align == "right":
                self.formatted_data[i] = f"{data}".rjust(data_x_size)

        # Recalculate and update y_size
        self.y_size = len(self.formatted_data)

    def __x_pad_cell(self):
        """Pads the left/right edges of the cell, regardless of alignment type"""
        # TODO: check for odd-number input handling
        for i, data in enumerate(self.formatted_data):
            self.formatted_data[i] = f"{data}".center(self.x_size)

    def resize_x(self, x_size: int) -> Self:
        """Triggers Cell reprocessing to fit the new x_size"""
        if x_size >= 0:
            self.x_size = x_size
            self.wrap_text()
            self.__x_align_data()
            self.__x_pad_cell()
        return self

    def resize_y(self, y_size: int) -> Self:
        """Add/removes list elements in formatted data to meet y_size requirements"""
        if y_size >= 0:
            # Assign y, trim formatted_data if too long
            self.y_size = y_size
            self.formatted_data = self.formatted_data[: self.y_size]
            # If too short, add filled whitespace strings to list
            while self.y_size > len(self.formatted_data):
                self.formatted_data.append(" " * self.x_size)
        return self

    def __str__(self) -> str:
        return "\n".join(self.formatted_data)
