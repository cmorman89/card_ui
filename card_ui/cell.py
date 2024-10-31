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
        self.raw_data = str(raw_data)
        self.formatted_data = []
        self.__x_size = 0
        self.__y_size = 0
        self.__y_window = 0
        self.__x_align = "left"

    # TODO `def process_newline_chars` in data = new line in cell

    @classmethod
    def new_cell(cls, raw_data):
        """Generate a valid, unformatted cell with data"""
        cell = cls(raw_data=raw_data)
        cell.format_x()
        return cell

    @property
    def x_size(self):
        """Returns the horizontal/x dimension of cell"""
        return self.__x_size

    @property
    def y_size(self):
        """Returns the vertical/y dimension of cell"""
        return self.__y_size

    @property
    def y_window(self):
        """Returns the y-window that limits rendered lines"""
        return self.__y_window

    # Public Methods

    def format_x(self, x_size: int = 0, x_align=None) -> Self:
        """Triggers Cell reprocessing to fit the new x_size"""
        if self.__x_size != x_size and x_size > 0:
            self.__x_size = x_size
        if self.__x_align != x_align and x_align is not None:
            self.__x_align = x_align
        self.__validate_x_size()
        self.__x_wrap_data()
        self.__x_align_data()

        # Make sure both dimensions of cell set initially
        self.__validate_y_window()
        return self

    def format_y_window(self, y_window: int) -> Self:
        """Adjusts the window size to meet display requirements"""
        # Set the window
        if y_window >= 0 and y_window != self.__y_window:
            self.__y_window = y_window
        # Expand if needed
        if y_window > self.__y_size:
            self.__y_expand_lines()
        # Or truncate extra space if needed
        # Note: render() limits actual output data!
        else:
            self.__y_truncate_lines()
        return self

    def render(self) -> str:
        """Generates the ouput `str`, limited by y-window size"""
        return "\n".join(self.formatted_data[: self.__y_window])

    # Private Methods

    def __x_align_data(self):
        """
        Aligns and fills whitespace to create a formatted string
        """
        # Align to available width
        data_x_size = self.__x_size
        for i, data in enumerate(self.formatted_data):
            if self.__x_align == "left":
                self.formatted_data[i] = f"{data}".ljust(data_x_size)
            elif self.__x_align == "center":
                self.formatted_data[i] = f"{data}".center(data_x_size)
            elif self.__x_align == "right":
                self.formatted_data[i] = f"{data}".rjust(data_x_size)

    def __x_wrap_data(self):
        """Wraps text into a list, splitting into multiple lines if needed"""
        if self.__x_size <= len(self.raw_data):
            self.formatted_data = textwrap.wrap(self.raw_data, self.__x_size)
        else:
            self.formatted_data = [self.raw_data]

        # Always recalc y_size after wrapping
        self.__y_size = len(self.formatted_data)

    def __y_expand_lines(self):
        """Adds lines of whitespace to fit y_window"""
        while self.__y_window > len(self.formatted_data):
            self.formatted_data.append(" " * self.__x_size)

    def __y_truncate_lines(self):
        """Removes lines of extra whitespace to fit y_window"""
        truncation_limit = min(self.__y_window, self.__y_size)
        self.formatted_data = self.formatted_data[:truncation_limit]

    def __validate_x_size(self):
        """Sets the initial x_size and fixes inalid sizes by fitting to all data"""
        self.__x_size = len(self.raw_data) if self.__x_size <= 0 else self.__x_size

    def __validate_y_window(self):
        """Sets the initial y_window to y_size; or leave as-is if already set"""
        self.__y_window = self.__y_size if self.__y_window <= 0 else self.__y_window

    def __str__(self) -> str:
        """Returns a formatted string representation of the cell, bound by y-window size"""
        return self.render()
