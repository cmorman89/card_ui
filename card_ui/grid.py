"""Grid is the parent object that holds grid data"""

from card_ui.cell import Cell
from card_ui.column import Column


class Grid:
    """Grid receives grid_data, and generates a matrix of cells before performing grid-
    related operations on the data"""

    def __init__(self, raw_grid_data):
        self.raw_grid_data = raw_grid_data
        self.grid_cells = []
        self.grid_cols = []
        self.grid_rows = []
        self.col_x_sizes = []

    def generate_cells(self):
        """Convert the raw_matrix_data to a matrix of Cells"""
        cell_matrix = []
        for rows in self.raw_grid_data:
            row_cells = [Cell.new_cell(raw_cell_data) for raw_cell_data in rows]
            cell_matrix.append(row_cells)
        self.grid_cells = cell_matrix

    # TODO: Future logic here after build Row class
    #    def generate_rows(self):
    #        for rows in self.grid_cells:
    #            row_obj = Row()
    #            for cell in rows:
    #                row_obj.add_cell(cell)

    def generate_cols(self):
        for cols in list(zip(*self.grid_cells)):
            col_obj = Column()
            for cell in cols:
                col_obj.add_cell(cell)
