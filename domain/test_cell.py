import unittest
from domain.cell import Cell

class TestCell(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_cell(self):
        cell = Cell(1, 2)
        self.assertEqual(cell.x, 1)
        self.assertEqual(cell.y, 2)
        self.assertEqual(cell.value, 0)

        cell.x = 3
        cell.y = 5
        cell.value = 6
        self.assertEqual(cell.x, 3)
        self.assertEqual(cell.y, 5)
        self.assertEqual(cell.value, 6)

