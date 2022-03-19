import math

import pygame
from repository.repo import Repository
from service.board_service import BoardService

class GUI:
    def __init__(self, service):
        self._serv = service
        self.game_over = False

        self.mode = "singleplayer"
        self.player_piece = 1
        self.ai_piece = 2

        self.BLUE = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.ROW_COUT = 15
        self.COLUMN_COUNT = 15

        self.EMPTY = 0
        self.CELL_SIZE = 40
        self.RADIUS = int(self.CELL_SIZE/2 - 5)
        self.width = self.COLUMN_COUNT * self.CELL_SIZE
        self.height = (self.ROW_COUT + 1) * self.CELL_SIZE

        self.WINDOW_LENGTH = 4
        
        self.CELL_SPACING = 5


    def draw_board(self, screen):
        board = self._serv.get_board_matrix()
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUT):
                pygame.draw.rect(screen, self.BLUE, ((c + 2) * self.CELL_SIZE - self.CELL_SIZE * 2,
                                                      (r + 1) * self.CELL_SIZE,
                                                      self.CELL_SIZE - self.CELL_SPACING,
                                                      self.CELL_SIZE - self.CELL_SPACING))
        for row in range(0, self.ROW_COUT):
            for col in range(0, self.COLUMN_COUNT):
                print(board[row][col], end=" ")
            print("")
        print("")
        for r in range(0, self.ROW_COUT):
            for c in range(0, self.COLUMN_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(screen, self.WHITE,
                                       (int(c * self.CELL_SIZE + self.CELL_SIZE / 2),
                                        int((r + 1) * self.CELL_SIZE + self.CELL_SIZE / 2)),
                                       self.RADIUS)
                elif board[r][c] == 2:
                    pygame.draw.circle(screen, self.BLACK,
                                       (int(c * self.CELL_SIZE + self.CELL_SIZE / 2),
                                        int((r + 1) * self.CELL_SIZE + self.CELL_SIZE / 2)),
                                       self.RADIUS)
        pygame.display.update()


    def start(self):
        game_over = False

        pygame.init()

        pygame.display.set_caption("Gomoku")

        screen = pygame.display.set_mode((self.width, self.height))

        text_rect = pygame.draw.rect(screen, self.BLACK,
                         (0, 0, self.CELL_SIZE * 7, self.CELL_SIZE - self.CELL_SPACING * 2))

        self.draw_board(screen)
        pygame.display.update()

        myfont = pygame.font.SysFont("monospace", 40)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over:
                        continue
                    pos_x = event.pos[0]
                    pos_y = event.pos[1]
                    y = int(math.floor(pos_x / self.CELL_SIZE)) + 1
                    x = int(math.floor(pos_y / self.CELL_SIZE))
                    if x == 0:
                        continue
                    #print(x, y)
                    if self.mode == "multiplayer":
                        if self._serv.is_empty_cell(x, y):
                            piece = self._serv.turn
                            self._serv.set_cell(x, y, self._serv.turn)
                            if self._serv.is_winner_move(x, y):
                                self.draw_board(screen)
                                if self._serv.turn == 1:
                                    message = "Black wins!"
                                else:
                                    message = "White wins!"
                                print(message)
                                text_surface_object = myfont.render(message, True, self.WHITE)
                                screen.blit(text_surface_object, text_rect)
                                self.game_over = True
                                pygame.display.flip()
                                continue
                            self.draw_board(screen)
                        else:
                            continue
                    else:
                        if self._serv.is_empty_cell(x, y):
                            self._serv.set_cell(x, y, self._serv.turn)
                            self._serv.last_move = (x, y)
                            if self._serv.is_winner_move(x, y):
                                self.draw_board(screen)
                                message = "White wins!"
                                print(message)
                                text_surface_object = myfont.render(message, True, self.WHITE)
                                screen.blit(text_surface_object, text_rect)
                                self.game_over = True
                                pygame.display.flip()
                                continue
                            else:
                                status = self._serv.ai_move(self._serv.turn)
                                if status == "ai win":
                                    message = "Black wins!"
                                    print(message)
                                    text_surface_object = myfont.render(message, True, self.WHITE)
                                    screen.blit(text_surface_object, text_rect)
                                    self.game_over = True
                                    pygame.display.flip()
                                    self.draw_board(screen)
                                    continue

                            self.draw_board(screen)
                        else:
                            continue



repo = Repository()
serv = BoardService(repo)
gui = GUI(serv)
gui.start()