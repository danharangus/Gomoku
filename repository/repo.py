import copy
from domain.cell import Cell


class Repository:
    def __init__(self):
        """
        Initializes the repository by creating a 15 by 15 array with cell objects having coordinates from 1 to 15
        """
        self._board = []
        for i in range(1, 16):
            for j in range(1, 16):
                self._board.append(Cell(i, j))

    def get_board(self):
        """
        Gets the board
        :return: list
        """
        return self._board

    def get_cell(self, x, y):
        """
        Gets the cell with the given coordinates
        :param x: int
        :param y: int
        :return: cell object
        """
        for cell in self._board:
            if cell.x == x and cell.y == y:
                return cell
        return None
