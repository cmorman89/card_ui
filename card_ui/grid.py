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
        self.grid_data_is_stale = True
        self.grid_format_is_stale = True

    # TODO: IMPORTANT! GENERATE DEFAULT GRID_CONFIG IF NOT PROVIDED ON ENTRY
    def update_grid(self, raw_grid_data=None, grid_config=None):
        """Primary entrypoint into Grid class."""

        # Update grid data
        if raw_grid_data != self.raw_grid_data:
            self.raw_grid_data = raw_grid_data
            self.__populate_grid()
            self.grid_data_is_stale = True

        # Update grid config
        if grid_config != self.grid_config:
            self.grid_config = grid_config
            # self.update_config()
            self.grid_format_is_stale = True

        # Trigger a repopulation/recalculation if needed
        if self.grid_data_is_stale:
            self.grid_format_is_stale = True
            # Always trigger a recalculation
            self.__populate_grid()

        if self.grid_format_is_stale:
            self.__format_grid()
            # TODO: Columns and Rows need to ensure their values are individually
            #       different before triggering a relalc

        return self

    # Methods to create and populate grid objects (Cells, Rows, Columns)
    def __populate_grid(self):
        """
        Generates the Cells that make up the grid, and adds them to Row and Column class
        objects. All are store in attributes in Grid object

        NOTE: This is the workflow to update grid *data*
        """
        # 1. Create the Cells
        self.__generate_cells()
        # 2. Create the Columns and add Cells
        self.__generate_cols()
        # 2. Create the Rows and add Cells
        self.__generate_rows()

    def __generate_cells(self):
        """Convert the raw_matrix_data to a matrix of Cells"""
        cell_matrix = []
        for rows in (
            self.raw_grid_data if self.raw_grid_data else []
        ):  # TODO: Else exception: Empty Grid
            row_cells = [Cell.new_cell(raw_cell_data) for raw_cell_data in rows]
            cell_matrix.append(row_cells)
        self.grid_cells = cell_matrix
        # TODO: Add row gaps and col gaps into matrix and then allow it to resize
        #       Even = data, odd = gap: [0:data][1:gap][2:data][n]
        # TODO: Make outside class for data input object

    def __generate_cols(self):
        """Creates Column objects and populates with Cell references"""
        grid_cols = []
        for cols in list(zip(*self.grid_cells)):
            col_obj = Column()
            for cell in cols:
                col_obj.add_cell(cell)
            grid_cols.append(col_obj)
        self.grid_cols = grid_cols

    def __generate_rows(self):
        """Creates Row objects and populates with Cell references"""
        grid_rows = []
        for rows in self.grid_cells:
            row_obj = Row()
            for cell in rows:
                row_obj.add_cell(cell)
            grid_rows.append(row_obj)
        self.grid_rows = grid_rows

    # Methods to format grid objects

    def __format_grid(self):
        """
        Uses the Row and Column classes to manage the formatting in their respective
        groups of cells

        NOTE: This is the workflow to update grid *formatting*
        """
        self.__format_grid_cols()
        self.__format_grid_rows()

    def __format_grid_cols(self):
        """Iterates the Column objects in grid and triggers a recalc/reformat"""
        for col in (
            self.grid_cols if self.grid_cols else []
        ):  # TODO: Else exception: Empty Columns
            col.format_x()

    def __format_grid_rows(self):
        """Iterates the Row objects in grid and triggers a recalc/reformat"""
        for row in (
            self.grid_rows if self.grid_rows else []
        ):  # TODO: Else exception: Empty Rows
            row.format_y()

    # TODO: Method group to render the grid
