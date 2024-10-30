import pytest
from card_ui.cell import Cell


def test_x_align_data_left():
    cell = Cell("test data")
    cell.format_x(20, "left")
    expected = ["test data           "]
    assert cell.formatted_data == expected


def test_x_align_data_center():
    cell = Cell("test data")
    cell.format_x(20, "center")
    expected = ["     test data      "]
    assert cell.formatted_data == expected


def test_x_align_data_right():
    cell = Cell("test data")
    cell.format_x(20, "right")
    expected = ["           test data"]
    assert cell.formatted_data == expected


def test_x_align_data_default():
    cell = Cell("test data")
    cell.format_x(20)
    expected = ["test data           "]
    assert cell.formatted_data == expected


def test_resize_x():
    cell = Cell("test data")
    cell.format_x(10)
    expected = ["test data "]
    assert cell.formatted_data == expected


def test_resize_y_increase():
    cell = Cell("test data")
    cell.format_x(10)
    cell.format_y_window(3)
    expected = ["test data ", "          ", "          "]
    assert cell.formatted_data == expected


def test_resize_y_decrease():
    cell = Cell("test data")
    cell.format_x(10)
    cell.format_y_window(1)
    expected = ["test data "]
    assert cell.formatted_data == expected


def test_wrap_text():
    cell = Cell("this is a long text that needs to be wrapped")
    cell.format_x(10)
    expected = ["this is a ", "long text ", "that needs", "to be     ", "wrapped   "]
    assert cell.formatted_data == expected


def test_render():
    cell = Cell("test data")
    cell.format_x(10)
    cell.format_y_window(1)
    expected = "test data "
    assert cell.render() == expected


def test_str_method():
    cell = Cell("test data")
    cell.format_x(10)
    cell.format_y_window(1)
    expected = "test data "
    assert str(cell) == expected


if __name__ == "__main__":
    pytest.main()
