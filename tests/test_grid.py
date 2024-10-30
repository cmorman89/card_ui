"""
Module for testing the Grid class from card_ui.
"""

import pytest
from card_ui.grid import Grid
from card_ui.cell import Cell


@pytest.fixture
def raw_grid_data_fixture():
    """Fixture for raw grid data."""
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.fixture
def grid_fixture(raw_grid_data_fixture):
    """Fixture for Grid instance."""
    return Grid(raw_grid_data_fixture)


def test_grid_initialization(grid_fixture, raw_grid_data_fixture):
    """Test the initialization of the Grid."""
    assert grid_fixture.raw_grid_data == raw_grid_data_fixture
    assert grid_fixture.grid_cells == []


def test_generate_cells(grid_fixture):
    """Test the generate_cells method of the Grid."""
    grid_fixture.generate_cells()
    assert len(grid_fixture.grid_cells) == 3
    assert all(
        isinstance(cell, Cell) for row in grid_fixture.grid_cells for cell in row
    )
    assert grid_fixture.grid_cells[0][0].raw_data == str(1)
    assert grid_fixture.grid_cells[1][1].raw_data == str(5)
    assert grid_fixture.grid_cells[2][2].raw_data == str(9)


def test_generate_cells_empty_data():
    """Test the generate_cells method with empty data."""
    empty_grid = Grid([])
    empty_grid.generate_cells()
    assert not empty_grid.grid_cells
