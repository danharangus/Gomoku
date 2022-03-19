import unittest
from board_service import BoardService
from repository.repo import Repository


class TestBoardService(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repository()
        self.serv = BoardService(self.repo)

    def tearDown(self) -> None:
        self.repo = None
        self.serv = None

    def test_board_service(self):
        self.serv.last_move = (0, 0)
        self.assertEquals(self.serv.last_move, (0, 0))
        self.assertEqual(self.serv.turn, 1)
        self.serv.turn = 2
        self.serv.set_cell(1, 1, 1)
        self.serv.set_cell(1, 1, 2)
        self.assertEqual(self.serv.get_board_matrix()[0][0], 2)
        self.assertEqual(self.serv.is_empty_cell(4, 4), True)
        self.assertEqual(self.serv.is_empty_cell(1, 1), False)

        self.serv.set_cell(5, 5, 1)
        self.serv.set_cell(5, 6, 1)
        self.serv.set_cell(5, 7, 1)
        self.serv.set_cell(5, 8, 1)
        self.serv.set_cell(5, 9, 1)

        self.serv.set_cell(4, 5, 1)
        self.serv.set_cell(5, 5, 1)
        self.serv.set_cell(6, 5, 1)
        self.serv.set_cell(7, 5, 1)
        self.serv.set_cell(8, 5, 1)

        self.serv.set_cell(5, 5, 1)
        self.serv.set_cell(6, 6, 1)
        self.serv.set_cell(7, 7, 1)
        self.serv.set_cell(4, 4, 1)
        self.serv.set_cell(8, 8, 1)

        self.serv.set_cell(5, 5, 1)
        self.serv.set_cell(4, 6, 1)
        self.serv.set_cell(3, 7, 1)
        self.serv.set_cell(6, 4, 1)
        self.serv.set_cell(7, 3, 1)

        board = self.serv.get_board_matrix()
        for row in board:
            for el in row:
                print(el, end=" ")
            print()
        self.assertEqual(self.serv.check_column(5, 5), 5)
        self.assertEqual(self.serv.check_line(5, 5), 5)
        self.assertEqual(self.serv.check_first_diagonal(5, 5), 5)
        self.assertEqual(self.serv.check_second_diagonal(5, 5), 5)
        self.assertEqual(self.serv.is_winner_move(5, 5), True)

        self.serv.set_cell(11, 10, 2)
        self.serv.set_cell(11, 11, 2)
        self.serv.set_cell(11, 12, 2)
        self.serv.ai_move(2)
        self.serv.ai_move(2)
        self.assertEquals(self.serv.is_winner_move(11, 12), True)
