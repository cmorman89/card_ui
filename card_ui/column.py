from typing import Self
from card_ui.cell import Cell


class Column:
    """Column holds a list of Cell obj references and manages dimensions and state of
    the column and x-attributes in a cell"""

    def __init__(self):
        self.col_cells = []
        self.col_x_size = 0
        self.col_min_x_size = 0
        self.col_max_x_size = 0

    def add_cell(self, cell: Cell) -> Self:
        """Add a cell to the column"""
        self.col_cells.append(cell)
        return self

    def set_col_x_size(self, col_x_size: int = 0):
        """Adjusts the col_x_sizes to fit largest column data"""
        # If size is different or zero/negative (invalid)
        if col_x_size != self.col_x_size or col_x_size <= 0:
            if col_x_size <= 0:
                # If invalid, use max cell x_size
                col_x_size = self.get_max_cell_x_size()
            self.col_x_size = col_x_size

            # Update cells with value
            self.__set_col_cell_x_sizes()

    def __set_col_cell_x_sizes(self):
        """Sets all member cell x_size to col_x_size"""
        for cell in self.col_cells:
            cell.format_x(self.col_x_size)

    def get_max_cell_x_size(self):
        """Returns the largest cell x_size in column"""
        return max([cell.x_size() for cell in self.col_cells])
