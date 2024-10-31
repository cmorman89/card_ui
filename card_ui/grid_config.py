"""The GridConfig class holds, validats, and manage default, global, and overriden
formatting information on the grid, column, row, or cell level"""

from dataclasses import dataclass, field


@dataclass
class GridConfig:
    """The GridConfig class holds, validats, and manage default, global, and overriden
    formatting information on the grid, column, row, or cell level"""

    # Global Settings and Defaults

    # Grid:
    # Grid x dimensions defaults
    grid_x_size: int = 100      # Not implemented yet
    grid_x_min_size: int = 0    # Not implemented yet
    grid_x_max_size: int = 0    # Not implemented yet
    grid_x_pad_size: int = 0    # Not implemented yet
    grid_x_align: str = "left"  # Not implemented yet
    # Grid y dimensions defaults
    grid_y_size: int = 0        # Not implemented yet
    grid_y_min_size: int = 0    # Not implemented yet
    grid_y_max_size: int = 0    # Not implemented yet
    grid_y_pad_size: int = 0    # Not implemented yet
    grid_y_align: str = "top"   # Not implemented yet

    # Column:
    # Col x dimension defaults
    col_x_min_size: int = 4     # Not implemented yet
    col_x_max_size: int = 0     # Not implemented yet
    col_gap_x_size: int = 1     # Not implemented yet
    # Col x attribute defaults

    row_y_min_size: int = 0     # Not implemented yet
    row_y_max_size: int = 0     # Not implemented yet

    row_gap_y_size: int = 0     # Not implemented yet

    # Column Overrides
    col_overrides: list = field(default_factory=list)
    # Row Overrides
