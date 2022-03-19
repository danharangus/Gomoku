import copy
import random


class BoardService:
    def __init__(self, repo):
        """
        Initializes the board service
        :param repo: repository object
        """
        self._repo = repo
        self._turn = 1
        self._last_move = (-1, -1)

    @property
    def turn(self):
        """
        Gets the current player turn (1 = white, 2 = black)
        :return: 1/2
        """
        return self._turn

    @turn.setter
    def turn(self, new_turn):
        """
        Sets the turn
        :param new_turn: 1/2
        """
        self._turn = new_turn

    @property
    def last_move(self):
        """
        Gets the last move made by the player
        """
        return self._last_move

    @last_move.setter
    def last_move(self, new_move):
        """
        Sets a new last move
        :param new_move: (int, int)
        """
        self._last_move = new_move

    def get_board_matrix(self):
        """
        Gets an array with indices from 0 to 15 containing the corresponding cell values
        :return: list of lists
        """
        board = self._repo.get_board()
        result = []
        for row in range(0, 15):
            result.append([])
            for col in range(0, 15):
                result[row].append(0)
        for cell in board:
            result[cell.x - 1][cell.y - 1] = cell.value
        return result

    def set_cell(self, x, y, val):
        """
        Sets the value of the cell with coordinates x and y to val
        :param x: int
        :param y: int
        :param val: int
        """
        cell = self._repo.get_cell(x, y)
        cell.value = val
        self.change_turn()
        #self._last_move = (x, y)

    def change_turn(self):
        """
        Changes the turn
        """
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def is_empty_cell(self, x, y):
        """
        Checks if the value of the cell with coordinates x, y is 0
        :param x: int
        :param y: int
        :return: True/False
        """
        cell = self._repo.get_cell(x, y)
        if cell is None or cell.value == 0:
            return True
        return False

    def check_line(self, x, y):
        """
        Checks if the cell at (x, y) is in a group of 5 on the its line
        :param x: int
        :param y: int
        :return: True/False
        """
        board = self.get_board_matrix()
        player = board[x - 1][y - 1]

        i = y - 1
        j = y - 1
        count = 0
        while i >= 0 and board[x - 1][i] == player:
            i -= 1
            count += 1
        while j < 15 and board[x - 1][j] == player:
            j += 1
            count += 1
        count -= 1
        return count

    def check_column(self, x, y):
        """
        Checks if the cell at (x, y) is in a group of 5 on the its column
        :param x: int
        :param y: int
        :return: True/False
        """
        board = self.get_board_matrix()
        player = board[x - 1][y - 1]
        i = x - 1
        j = x - 1
        count = 0
        while i >= 0 and board[i][y - 1] == player:
            i -= 1
            count += 1
        while j < 15 and board[j][y - 1] == player:
            j += 1
            count += 1
        count -= 1
        return count

    def check_first_diagonal(self, x, y):
        """
        Checks if the cell at (x, y) is in a group of 5 on the its first diagonal
        :param x: int
        :param y: int
        :return: True/False
        """
        board = self.get_board_matrix()
        player = board[x - 1][y - 1]

        i1 = i2 = x - 1
        j1 = j2 = y - 1
        count = 0
        while i1 >= 0 and j1 >= 0 and board[i1][j1] == player:
            i1 -= 1
            j1 -= 1
            count += 1

        while i2 < 15 and j2 < 15 and board[i2][j2] == player:
            i2 += 1
            j2 += 1
            count += 1

        count -= 1
        #print(count)
        return count

    def check_second_diagonal(self, x, y):
        """
        Checks if the cell at (x, y) is in a group of 5 on the its second diagonal
        :param x: int
        :param y: int
        :return: True/False
        """
        board = self.get_board_matrix()
        player = board[x - 1][y - 1]

        i1 = i2 = x - 1
        j1 = j2 = y - 1
        count = 0
        while i1 >= 0 and j1 < 15 and board[i1][j1] == player:
            i1 -= 1
            j1 += 1
            count += 1

        while i2 < 15 and j2 >= 0 and board[i2][j2] == player:
            i2 += 1
            j2 -= 1
            count += 1

        count -= 1
        #print(count)
        return count

    def is_winner_move(self, x, y):
        """
        Checks if the piece placed at (x, y) completes a group of at least five and thus wins the game
        :param x: int
        :param y: int
        :return: True/False
        """
        if self.check_line(x, y) >= 5 \
                or self.check_column(x, y) >= 5\
                or self.check_first_diagonal(x, y) >= 5 \
                or self.check_second_diagonal(x, y) >= 5:
            return True
        return False

    def ai_move(self, piece):
        """
        Performs an AI move
        :param piece: AI piece
        :return: "ai win" if the ai won in the last move
        """
        board = self.get_board_matrix()
        last_x, last_y = self._last_move

        for i in range(0, 15):
            for j in range(0, 15):
                if board[i][j] == piece:
                    if self.check_column(i + 1, j + 1) >= 3:
                        x = i
                        while x < 14 and board[x][j] == piece:
                            x += 1
                        if self.is_empty_cell(x + 1, j + 1):
                            self.set_cell(x + 1, j + 1, piece)
                            if self.is_winner_move(x + 1, j + 1):
                                return "ai win"
                            return

                        x = i
                        while x > 0 and board[x][j] == piece:
                            x -= 1
                        if self.is_empty_cell(x + 1, j + 1):
                            self.set_cell(x + 1, j + 1, piece)
                            if self.is_winner_move(x + 1, j + 1):
                                return "ai win"
                            return
                    if self.check_line(i + 1, j + 1) >= 3:
                        y = j
                        while y < 14 and board[i][y] == piece:
                            y += 1
                        if self.is_empty_cell(i + 1, y + 1):
                            self.set_cell(i + 1, y + 1, piece)
                            if self.is_winner_move(i + 1, y + 1):
                                return "ai win"
                            return

                        y = j
                        while y >= 0 and board[i][y] == piece:
                            y -= 1
                        if self.is_empty_cell(i + 1, y + 1):
                            self.set_cell(i + 1, y + 1, piece)
                            if self.is_winner_move(i + 1, y + 1):
                                return "ai win"
                            return

                    if self.check_first_diagonal(i + 1, j + 1) >= 3:
                        x, y = i, j
                        while x < 14 and y < 14 and board[x][y] == piece:
                            y += 1
                            x += 1
                        if self.is_empty_cell(x + 1, y + 1):
                            self.set_cell(x + 1, y + 1, piece)
                            if self.is_winner_move(x + 1, y + 1):
                                return "ai win"
                            return

                        x, y = i, j
                        while y > 0 and x > 0 and board[x][y] == piece:
                            y -= 1
                            x -= 1
                        if self.is_empty_cell(x + 1, y + 1):
                            self.set_cell(x + 1, y + 1, piece)
                            if self.is_winner_move(x + 1, y + 1):
                                return "ai win"
                            return

                    if self.check_second_diagonal(i + 1, j + 1) >= 3:
                        x, y = i, j
                        while x < 14 and y > 0 and board[x][y] == piece:
                            y -= 1
                            x += 1
                        if self.is_empty_cell(x + 1, y + 1):
                            self.set_cell(x + 1, y + 1, piece)
                            if self.is_winner_move(x + 1, y + 1):
                                return "ai win"
                            return

                        x, y = i, j
                        while y < 14 and x > 0 and board[x][y] == piece:
                            y += 1
                            x -= 1
                        if self.is_empty_cell(x + 1, y + 1):
                            self.set_cell(x + 1, y + 1, piece)
                            if self.is_winner_move(x + 1, y + 1):
                                return "ai win"
                            return

        player_piece = 1
        if self.check_column(last_x, last_y) >= 2:
            i = j = last_x - 1
            while i >= 0 and board[i][last_y - 1] == player_piece:
                i -= 1
            if i > 0 and i < 14 and self.is_empty_cell(i + 1, last_y):
                self.set_cell(i + 1, last_y, piece)
                if self.is_winner_move(i + 1, last_y):
                    return "ai win"
                return
            else:
                while j < 14 and board[j][last_y - 1] == player_piece:
                    j += 1
                if self.is_empty_cell(j + 1, last_y):
                    self.set_cell(j + 1, last_y, piece)
                    if self.is_winner_move(j + 1, last_y):
                        return "ai win"
                    return
        elif self.check_line(last_x, last_y) >= 2:
            i = j = last_y - 1
            while i > 0 and board[last_x - 1][i] == player_piece:
                i -= 1
            if self.is_empty_cell(last_x, i + 1):
                self.set_cell(last_x, i + 1, piece)
                if self.is_winner_move(last_x, i + 1):
                    return "ai win"
                return
            else:
                while j < 14 and board[last_x - 1][j] == player_piece:
                    j += 1
                if self.is_empty_cell(last_x, j + 1):
                    self.set_cell(last_x, j + 1, piece)
                    if self.is_winner_move(last_x, j + 1):
                        return "ai win"
                    return
        elif self.check_first_diagonal(last_x, last_y) >= 2:
            i , j = last_x - 1, last_y - 1
            while i > 0 and j > 0 and board[i][j] == player_piece:
                i -= 1
                j -= 1
            if self.is_empty_cell(i + 1, j + 1):
                self.set_cell(i + 1, j + 1, piece)
                if self.is_winner_move(i + 1, j + 1):
                    return "ai win"
                return
            else:
                i, j = last_x - 1, last_y - 1
                while i < 14 and j < 14 and board[i][j] == player_piece:
                    i += 1
                    j += 1
                if self.is_empty_cell(i + 1, j + 1):
                    self.set_cell(i + 1, j + 1, piece)
                    if self.is_winner_move(i + 1, j + 1):
                        return "ai win"
                    return

        elif self.check_second_diagonal(last_x, last_y) >= 2:
            i, j = last_x - 1, last_y - 1
            while i > 0 and j < 14 and board[i][j] == player_piece:
                i -= 1
                j += 1
            if self.is_empty_cell(i + 1, j + 1):
                self.set_cell(i + 1, j + 1, piece)
                if self.is_winner_move(i + 1, j + 1):
                    return "ai win"
                return
            else:
                i, j = last_x - 1, last_y - 1
                while i < 14 and j > 0 and board[i][j] == player_piece:
                    i += 1
                    j -= 1
                if self.is_empty_cell(i + 1, j + 1):
                    self.set_cell(i + 1, j + 1, piece)
                    if self.is_winner_move(i + 1, j + 1):
                        return "ai win"
                    return
        else:
            move = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, 0), (-1, -1)]
            random.shuffle(move)
            k = 0
            while k < 8:
                next_x, next_y = last_x + move[k][0], last_y + move[k][1]
                if 1 <= next_x <= 15 and 1 <= next_y <= 15:
                    if self.is_empty_cell(next_x, next_y):
                        self.set_cell(next_x, next_y, piece)
                        if self.is_winner_move(next_x, next_y):
                            return "ai win"
                        return
                k += 1

        x = random.randint(1, 15)
        y = random.randint(1, 15)
        while self._repo.get_cell(x, y) is not None and not self.is_empty_cell(x, y):
            x = random.randint(1, 15)
            y = random.randint(1, 15)
        self.set_cell(x, y, piece)
        if self.is_winner_move(x, y):
            #print("ai win")
            return "ai win"

