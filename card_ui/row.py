from typing import Self
from card_ui.cell import Cell


class Row:
    """Row holds a list of Cell obj references and manages dimensions and state of
    the column and x-attributes in a cell"""

    def __init__(self):
        self.row_cells = []
        self.row_y_size = 0
        self.row_min_y_size = 0
        self.row_max_y_size = 0

    def format_y(self, row_y_size: int = 0):
        """Trigger column format calculations"""
        self.__set_row_y_size(row_y_size)

    def add_cell(self, cell: Cell) -> Self:
        """Add a cell to the row"""
        self.row_cells.append(cell)
        return self

    def __set_row_y_size(self, row_y_size: int = 0):
        """Adjusts the row_y_sizes to fit largest row data"""
        # If size is different or zero/negative (invalid)
        if row_y_size != self.row_y_size or row_y_size <= 0:
            if row_y_size <= 0:
                row_y_size = self.get_max_cell_y_size()
            self.row_y_size = row_y_size

            # Update cells with value
            self.__set_row_cell_y_windows()

    def __set_row_cell_y_windows(self):
        """Sets all member cell y_windows to row_y_size"""
        for cell in self.row_cells:
            cell.format_y_window(self.row_y_size)

    def get_max_cell_y_size(self):
        """Returns the largest cell y_size in row"""
        return max([cell.y_size for cell in self.row_cells])

    def get_row_y_lines(self):
        """Gets cell lines, transposes, and combines to create row lines in a list
        separated by cell"""
        return [list(row) for row in zip(*(cell.render() for cell in self.row_cells))]
