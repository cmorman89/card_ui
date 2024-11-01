"""This is currently just a demo file"""

import os
import sys
import time
import shutil  # for terminal size calculation
from card_ui.grid import Grid

GRID_DELAY = 0.15
matrix = [
    [
        "Strategic Attack Plan",
        "Reason beyond perception",
        "Initiate Pull Sequence",
        "Conference under the grand tree of possibilities",
    ],
    [
        "Reflect deeply on PM schedule",
        "Ever-changing circumstances dictate choices",
        "Step into unknown realms",
        "Through the vast expanse of the church's history and significance",
    ],
    [
        "Taking Note of Critical Issues",
        "Live practice and experiential growth",
        "Expanding the economic camera lens",
        "Contemplate five essential pillars to build upon",
    ],
    [
        "Value remains the same over decades",
        "Send strong signals across regions",
        "Machine learning: guess and improve",
        "Breaking through barriers in the last phase",
    ],
    [
        "Provide consistent support system",
        "Behavioral insights for board term analysis",
        "Military room configurations for optimal response",
        "Social networks strengthen community bonds",
    ],
    [
        "Sell as a final resort",
        "Class boundaries in marriage traditions",
        "City planning with sustainable goals",
        "Producing outcomes with shared effort",
    ],
    [
        "Marriage theories prove economic resilience",
        "Election fund allocation and results",
        "Scheduling pivotal meetings",
        "The common ground in cultural contexts",
    ],
    [
        "Forward-looking strategies",
        "Actionable insights from case studies",
        "Coordinate resources effectively",
        "Reconcile diverse perspectives for unified goals",
    ],
    [
        "Harnessing renewable energy sources",
        "Behavioral trends in urban populations",
        "Expansion of metropolitan areas",
        "Social adaptation in climate response",
    ],
    [
        "Innovation in technological advancement",
        "Learning paths across sectors",
        "Initiating community outreach",
        "Partnerships in global development",
    ],
]


def clear_terminal():
    """Fully clears the terminal including scrollback and resets cursor to top-left."""
    print("\033[H", end="")  # Clear screen and scrollback buffer, resets cursor to 0,0


def calculate_rendered_lines(grid):
    """Calculates the number of lines needed to render the grid content and borders."""
    content_rows = len(grid.grid_rows)
    lines_per_content_row = max(len(row.get_row_y_lines()) for row in grid.grid_rows)
    total_content_lines = content_rows * lines_per_content_row
    total_border_lines = content_rows - 1  # Only count middle borders

    return (
        2 + total_content_lines + total_border_lines
    )  # top + bottom border, middle borders, content rows


def fill_remaining_terminal_space(rendered_lines, terminal_height):
    """Fills only the exact remaining space in the terminal after rendered lines."""
    terminal_size = shutil.get_terminal_size()  # use shutil to get terminal size
    for _ in range(terminal_height - rendered_lines):
        print(" " * terminal_size.columns)


def move_cursor_up_two_rows():
    """Moves the terminal cursor up by two rows."""
    print("\033[5A", end="")


def print_grid_with_grow_effect(grid, delay=GRID_DELAY):
    """Prints the grid with a growing width effect."""
    terminal_size = shutil.get_terminal_size()  # use shutil to get terminal size
    terminal_width = terminal_size.columns
    terminal_height = terminal_size.lines
    max_width = (terminal_width - 18) // 4
    # Clear term first
    print("\033c", end="")
    for x_size in range(8, max_width + 1):
        # Clear screen before every render to avoid leftover content
        clear_terminal()

        # Update grid formatting with new x_size
        grid.format_grid(temp_x=x_size, temp_x_align="center")

        # Render borders
        top_border = "┌" + ("─" * (x_size + 2) + "┬") * 3 + ("─" * (x_size + 2)) + "┐"
        middle_border = (
            "├" + ("─" * (x_size + 2) + "┼") * 3 + ("─" * (x_size + 2)) + "┤"
        )
        bottom_border = (
            "└" + ("─" * (x_size + 2) + "┴") * 3 + ("─" * (x_size + 2)) + "┘"
        )

        # Prepare lines to print
        output_lines = [f"Matrix in a grid with col_x_size = {x_size}:"]
        output_lines.append(top_border)

        for i, row in enumerate(grid.grid_rows):
            formatted_row = [
                " │ ".join("".join(cell) for cell in line)
                for line in row.get_row_y_lines()
            ]
            output_lines.append("│ " + " │\n│ ".join(formatted_row) + " │")
            if i < len(grid.grid_rows) - 1:
                output_lines.append(middle_border)

        output_lines.append(bottom_border)

        # Calculate rendered lines accurately and print output lines
        rendered_lines = calculate_rendered_lines(grid)
        for line in output_lines:
            print(line)
        fill_remaining_terminal_space(rendered_lines, terminal_height)

        time.sleep(delay)
    # clear_terminal()


# Initialize and format grid
grid = Grid(matrix)
grid.update_grid(temp_x_align="right")

# Run the growing effect print
print_grid_with_grow_effect(grid)
move_cursor_up_two_rows()
# time.sleep(1000)
