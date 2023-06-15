# TicTacToe Game using Oop and Pygame by Sami

# Python Libraries
import pygame
import sys

# Class function with constructor and parameters.
class TicTacToe:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Constants
        self.WIDTH = 600
        self.HEIGHT = 600
        self.LINEWIDTH = 10
        self.BOARDSIZE = 3
        self.BOARDCOLOR = (255, 255, 255)
        self.LINECOLOR = (0, 0, 0)
        self.PLAYER1COLOR = (255, 0, 0)
        self.PLAYER2COLOR = (0, 0, 255)

        # Create the game window
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")

        # Create the game board
        self.board = [[' ' for _ in range(self.BOARDSIZE)] for _ in range(self.BOARDSIZE)]

        # Initialize current player
        self.current_player = 'X'

    # Function to draw the game board
    def drawboard(self):
        self.window.fill(self.BOARDCOLOR)

        # Draw horizontal lines
        for row in range(1, self.BOARDSIZE):
            y = row * self.HEIGHT // self.BOARDSIZE
            pygame.draw.line(self.window, self.LINECOLOR, (0, y), (self.WIDTH, y), self.LINEWIDTH)

        # Draw vertical lines
        for col in range(1, self.BOARDSIZE):
            x = col * self.WIDTH // self.BOARDSIZE
            pygame.draw.line(self.window, self.LINECOLOR, (x, 0), (x, self.HEIGHT), self.LINEWIDTH)

        # Draw X's and O's
        for row in range(self.BOARDSIZE):
            for col in range(self.BOARDSIZE):
                if self.board[row][col] == 'X':
                    self.drawx(row, col)
                elif self.board[row][col] == 'O':
                    self.drawo(row, col)

        pygame.display.update()  # Update the display

    # Function to draw an X at the given position
    def drawx(self, row, col):
        cellwidth = self.WIDTH // self.BOARDSIZE
        cellheight = self.HEIGHT // self.BOARDSIZE

        x = col * cellwidth + cellwidth // 2
        y = row * cellheight + cellheight // 2

        halfsize = min(cellwidth, cellheight) // 4
        pygame.draw.line(self.window, self.PLAYER1COLOR, (x - halfsize, y - halfsize), (x + halfsize, y + halfsize), self.LINEWIDTH)
        pygame.draw.line(self.window, self.PLAYER1COLOR, (x - halfsize, y + halfsize), (x + halfsize, y - halfsize), self.LINEWIDTH)

    # Function to draw an O at the given position
    def drawo(self, row, col):
        cellwidth = self.WIDTH // self.BOARDSIZE
        cellheight = self.HEIGHT // self.BOARDSIZE

        x = col * cellwidth + cellwidth // 2
        y = row * cellheight + cellheight // 2

        radius = min(cellwidth, cellheight) // 4
        pygame.draw.circle(self.window, self.PLAYER2COLOR, (x, y), radius, self.LINEWIDTH)

    # Function to check if a player has won
    def checkwin(self, player):
        # Check rows
        for row in range(self.BOARDSIZE):
            if all(self.board[row][col] == player for col in range(self.BOARDSIZE)):
                return True

        # Check columns
        for col in range(self.BOARDSIZE):
            if all(self.board[row][col] == player for row in range(self.BOARDSIZE)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(self.BOARDSIZE)):
            return True

        if all(self.board[i][self.BOARDSIZE - i - 1] == player for i in range(self.BOARDSIZE)):
            return True

        return False

    # Main game loop
    def gameloop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:  # Left mouse button
                        pos = pygame.mouse.get_pos()
                        row = pos[1] // (self.HEIGHT // self.BOARDSIZE)
                        col = pos[0] // (self.WIDTH // self.BOARDSIZE)

                        if self.board[row][col] == ' ':
                            self.board[row][col] = self.current_player
                            self.drawboard()

                            if self.checkwin(self.current_player):
                                print(f"Player {self.current_player} wins!")
                                pygame.time.wait(3000)
                                pygame.quit()
                                sys.exit()

                            if self.current_player == 'X':
                                self.current_player = 'O'
                            else:
                                self.current_player = 'X'


# Start the game
game = TicTacToe()
game.drawboard()  # Call drawboard to display the initial game board
game.gameloop()
