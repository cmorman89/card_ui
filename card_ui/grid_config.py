"""The GridConfig class holds, validates, and manage default, global, and overridden
formatting information on the grid, column, row, or cell level"""


class GridConfig:
    """The GridConfig class holds, validates, and manage default, global, and overridden
    formatting information on the grid, column, row, or cell level"""

    def __init__(self):

        # `config` holds global settings and defaults
        self.global_config = {
            "grid": {
                "size": {
                    "x": {"default": 100, "min": 0, "max": 200, "padding": 0},
                    "y": {"default": 100, "min": 0, "max": 200, "padding": 0},
                }
            },
            "column": {
                "size": {"x": {"min": 4, "max": 100, "gap": 1, "alignment": "left"}}
            },
            "row": {
                "size": {
                    "y": {
                        "min": 0,
                        "max": 100,
                        "gap": 1,
                        "alignment": "top",
                    }
                }
            },
        }

        # `override` holds individual Column and Row-level overrides to the global
        # default config settings
        self.override = {
            "columns": {
                0: {  # Overrides for column 0
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                1: {  # Overrides for column 1
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                2: {  # Overrides for column 2
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                3: {  # Overrides for column 3
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                4: {  # Overrides for column 4
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                # Note: Add more if needed
            },
            "rows": {
                0: {  # Overrides for row 0
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                1: {  # Overrides for row 1
                    "size": {
                        "x": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                        "y": {
                            "default": None,
                            "min": None,
                            "max": None,
                            "padding": None,
                            "alignment": None,
                        },
                    }
                },
                # Note: Add more if needed
            },
        }

        # `state` holds the actual, active/pending grid formatting data
        self.state = {
            "data_is_stale": True,  # Indicates if grid data needs to be recalculated
            "format_is_stale": True,  # Indicates if grid formatting needs to be recalculated
            "grid": {
                "dynamic_space": None,  # Placeholder for dynamic space adjustments
            },
            "columns": [],
            "rows": [],
        }

    def get_global_value(self, *keys, default=None):
        """Safely access config data and handle missing keys"""
        config = self.global_config
        try:
            for key in keys:
                config = config[key]
            return config
        except KeyError:
            return default

    # Calculate column width allocations
    def __calc_col_x_sizes(self):
        # TODO: Get the total number of columns
        # TODO: Get the total dynamic space
        # TODO: Allocate dynamic space to cols
        self.__set_num_columns()
        num_cols = self.get_global_value

    def __set_num_columns(
        self, num_cols: int = 0, raw_grid_data: list = [None], grid=None
    ):
        """Calculates the number of columns from the raw_grid_data or from input"""
        count = 0
        if num_cols >= 0:
            """Explicitly provided column count takes precedence"""
            count = num_cols
        elif raw_grid_data:
            count = len(list(zip(*raw_grid_data)))
        elif grid:
            count = len(grid.grid_cols)
        # Update value
        self.num_cols = count if count >= 0 else self.num_cols

    def __set_column_widths(self):
        """Calculates and allocates available space to columns"""
