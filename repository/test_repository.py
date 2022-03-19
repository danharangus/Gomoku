import unittest
from repository.repo import Repository


class TestRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = Repository()

    def tearDown(self) -> None:
        self.repo = None

    def test_repo(self):
        board = self.repo.get_board()
        self.assertEqual(len(board), 15 * 15)

        cell = self.repo.get_cell(1, 2)
        cell.value = 5
        self.assertEqual(self.repo.get_cell(1, 2).value, 5)
        self.assertEqual(self.repo.get_cell(16, 16), None)
