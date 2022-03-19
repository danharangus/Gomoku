from repository.repo import Repository
from service.board_service import BoardService


class ConsoleUI:
    def __init__(self, service):
        self._serv = service
        self._mode = "singleplayer"

    def draw_board(self):
        board = self._serv.get_board_matrix()
        for row in board:
            for el in row:
                print(el, end=" ")
            print("")
        print("")

    def get_move(self):
        try:
            x = int(input("x: "))
            if x < 1 or x > 16:
                print("Error: The position must be an integer between 1 and 19")
                return
        except ValueError as ve:
            print("Error: The position must be an integer between 1 and 19")
            return
        try:
            y = int(input("y: "))
            if y < 1 or y > 16:
                print("Error: The position must be an integer between 1 and 19")
                return
        except ValueError as ve:
            print("Error: The position must be an integer between 1 and 19")
            return

        return x, y

    def start(self):
        while True:
            self.draw_board()
            print("1. Move")
            print("2. Exit")
            try:
                command = int(input(">>"))
            except ValueError as ve:
                print("Invalid command")
                continue
            if command == 2:
                return
            elif command == 1:
                try:
                    x, y = self.get_move()
                except:
                    continue
                if self._mode == "multiplayer":
                    if self._serv.is_empty_cell(x, y):
                        self._serv.set_cell(x, y, self._serv.turn)
                        self._serv.last_move = (x, y)
                        if self._serv.is_winner_move(x, y):
                            self.draw_board()
                            print("Player wins!")
                            return
                    else:
                        print("Given cell is already occupied.")
                        continue
                else:
                    if self._serv.is_empty_cell(x, y):
                        self._serv.set_cell(x, y, self._serv.turn)
                        self._serv.last_move = (x, y)
                        if self._serv.is_winner_move(x, y):
                            self.draw_board()
                            print("Player wins!")
                            return
                        else:
                            status = self._serv.ai_move(self._serv.turn)
                            if status == "ai win":
                                message = "Black wins!"
                                print(message)
                                return
                    else:
                        print("Given cell is already occupied.")
                        continue


            else:
                print("Invalid command")


repo = Repository()
serv = BoardService(repo)
ui = ConsoleUI(serv)
ui.start()


