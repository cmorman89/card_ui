"""Grid is the parent object that holds grid data"""

from card_ui.cell import Cell


class Grid:
    """Grid receives grid_data, and generates a matrix of cells before performing grid-
    related operations on the data"""

    def __init__(self, raw_grid_data):
        self.raw_grid_data = raw_grid_data
        self.grid_cells = []

    def generate_cells(self):
        """Convert the raw_matrix_data to a matrix of Cells"""
        cell_matrix = []
        for rows in self.raw_grid_data:
            row_cells = [Cell.new_cell(raw_cell_data) for raw_cell_data in rows]
            cell_matrix.append(row_cells)
        self.grid_cells = cell_matrix
