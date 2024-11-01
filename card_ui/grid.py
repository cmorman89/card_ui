"""Grid is the parent object that holds grid data"""

from card_ui.cell import Cell
from card_ui.column import Column
from card_ui.row import Row


class Grid:
    """Grid receives grid_data, and generates a matrix of cells before performing grid-
    related operations on the data"""

    def __init__(self, raw_grid_data, grid_config=None):
        self.raw_grid_data = raw_grid_data
        self.grid_config = grid_config
        self.grid_cells = []
        self.grid_cols = []
        self.grid_rows = []

    def format_grid(
        self,
        raw_grid_data=None,
        grid_config=None,
        temp_x=0,
        temp_y=0,
        temp_x_align="right",
    ):
        self.generate_cells()
        self.generate_cols()
        self.generate_rows()
        # TODO: self.format_cols()
        # TODO: self.format_row()
        [
            col.format_x(temp_x, col_x_align=temp_x_align) for col in self.grid_cols
        ]  # TODO: REMOVE temp x
        [row.format_y(temp_y) for row in self.grid_rows]  # TODO: REMOVE temp y
        return self

    def generate_cells(self):
        # TODO: Add row gaps and col gaps into matrix and then allow it to resize
        #       Even = data, odd = gap: [0:data][1:gap][2:data][n]
        # TODO: Make outside class for data input object
        """Convert the raw_matrix_data to a matrix of Cells"""
        cell_matrix = []
        for rows in self.raw_grid_data:
            row_cells = [Cell.new_cell(raw_cell_data) for raw_cell_data in rows]
            cell_matrix.append(row_cells)
        self.grid_cells = cell_matrix

    def generate_cols(self):
        grid_cols = []
        for cols in list(zip(*self.grid_cells)):
            col_obj = Column()
            for cell in cols:
                col_obj.add_cell(cell)
            grid_cols.append(col_obj)
        self.grid_cols = grid_cols

    def generate_rows(self):
        grid_rows = []
        for rows in self.grid_cells:
            row_obj = Row()
            for cell in rows:
                row_obj.add_cell(cell)
            grid_rows.append(row_obj)
        self.grid_rows = grid_rows
