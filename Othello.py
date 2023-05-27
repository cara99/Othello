# Author: Keirah Jefferson
# GitHub: cara99
# Date: 5/19/22023
# Description: A program that allows two people to play Othello

from run_game import *
class Player:
    """The Player class represents a player in the game. The player class
    is responsible for storing the names and colors of the players
    in the game"""

    def __init__(self, player_name, color):
        """Player name and color"""
        self._player_name = player_name

        # ensure input is lowercase
        self._color = color.lower()

    def get_player_name(self):
        """Returns the player's name"""
        return str(self._player_name)

    def get_player_color(self):
        """Returns the player's color"""
        return self._color


class Othello:
    """Class represent the Othello Game Board. It contains
     information about the players and the board. Othello must print the board,
     create players on the board by calling Player class,
     return who the winner is, return available positions to be played,
     allow players to make a move, and allow players to play the game and announce when the game is over,"""

    def __init__(self):
        """Creates a game Board.
        Initialize the game board as a 10x10 grid represented by a 2D array"""
        self._board = []
        self._players = []  # A list of PLayer objects
        self._white_pieces = 2
        self._black_pieces = 2

        # Each board row is initialized by default
        self._board.append(["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"])
        self._board.append(["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"])
        self._board.append(["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"])
        self._board.append(["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"])

    def get_board(self):
        """Returns the current game board"""
        return self._board
    def get_white_pieces(self):
        """Returns the white pieces on the board"""
        return self._white_pieces
    def get_black_pieces(self):
        """Returns the black pieces on the board"""
        return self._black_pieces
    def print_board(self):
        """Prints out the current board, including the boundaries"""
        for row in self._board:
            print('  '.join(row))

    def create_player(self, player_name, color):
        """Creates a player object with the given name and color,
        then adds it to the player list"""
        self._players.append(Player(player_name, color))

    def return_available_positions(self, color):
        """Returns a list of tuples for the player with the given
        color to move on the current board"""

        # Initialize an empty list of available positions (row, column) set on the board
        # this just shows the free positions
        available_positions = set()

        # Figure out if this is the white or black player
        self_piece, opposite_piece = ("X", "O") if color == "black" else ("O", "X")
        for row in range(0, len(self._board) - 1):
            for column in range(0, len(self._board) - 1):
                if self._board[row][column] == opposite_piece:  # Found a black puzzle piece
                    if self._board[row][column - 1] == self_piece:
                        # Found a white puzzle piece to the left
                        for num in range(1, len(self._board)):
                            if self._board[row][column + num] == ".":
                                available_positions.add((row, column + num))
                                break
                            elif self._board[row][column + num] == self_piece:
                                break
                            elif self._board[row][column + num] == "*":
                                break
                            # Repeat for top, top right, right, bottom right, bottom, bottom left
                    # Right
                    if self._board[row][column + 1] == self_piece:
                        # Found a white puzzle piece to the right
                        for num in range(1, len(self._board)):
                            if self._board[row][column - num] == ".":
                                available_positions.add((row, column - num))
                                break
                            elif self._board[row][column - num] == self_piece:
                                break
                            elif self._board[row][column - num] == "*":
                                break
                    # Down
                    if self._board[row + 1][column] == self_piece:
                        # Found a white puzzle piece to the top
                        for num in range(1, len(self._board)):
                            if self._board[row - num][column] == ".":
                                available_positions.add((row - num, column))
                                break
                            elif self._board[row - num][column] == self_piece:
                                break
                            elif self._board[row - num][column] == "*":
                                break
                    # Up
                    if self._board[row - 1][column] == self_piece:
                        # Found a white piece to the bottom
                        for num in range(1, len(self._board)):
                            if self._board[row + num][column] == ".":
                                available_positions.add((row + num, column))
                                break
                            elif self._board[row + num][column] == self_piece:
                                break
                            elif self._board[row + num][column] == "*":
                                break
                    # Bottom right
                    if self._board[row + 1][column + 1] == self_piece:
                        # found a white piece to the top right
                        for num in range(1, len(self._board)):
                            if self._board[row - num][column - num] == ".":
                                available_positions.add((row - num, column - num))
                                break
                            elif self._board[row - num][column - num] == self_piece:
                                break
                            elif self._board[row - num][column - num] == "*":
                                break
                    # Bottom left
                    if self._board[row + 1][column - 1] == self_piece:
                        for num in range(1, len(self._board)):
                            if self._board[row - num][column + num] == ".":
                                available_positions.add((row - num, column + num))
                                break
                            elif self._board[row - num][column + num] == self_piece:
                                break
                            elif self._board[row - num][column + num] == "*":
                                break
                    # Top left
                    if self._board[row - 1][column - 1] == self_piece:
                        for num in range(1, len(self._board)):
                            if self._board[row + num][column + num] == ".":
                                available_positions.add((row + num, column + num))
                                break
                            elif self._board[row + num][column + num] == self_piece:
                                break
                            elif self._board[row + num][column + num] == "*":
                                break
                    # Top right
                    if self._board[row - 1][column + 1] == self_piece:
                        for num in range(1, len(self._board)):
                            if self._board[row + num][column - num] == ".":
                                available_positions.add((row + num, column - num))
                                break
                            elif self._board[row + num][column - num] == self_piece:
                                break
                            elif self._board[row + num][column - num] == "*":
                                break
        return list(sorted(available_positions, key=lambda position: (position[0], position[1])))

    def return_winner(self):
        """Returns winner announcement"""
        num_white = 0
        num_black = 0

        for row in range(1, len(self._board)):
            for index in range(1, len(self._board)):
                if self._board[row][index] == "O":
                    num_white += 1
                elif self._board[row][index] == "X":
                    num_black += 1

        self._white_pieces = num_white
        self._black_pieces = num_black

        if num_white > num_black and self._players[0].get_player_color == "white":
            white_player = self._players[0]
            return "Winner is white player: " + white_player.get_player_name()

        elif num_white > num_black and self._players[1].get_player_color == "white":
            white_player = self._players[1]
            return "Winner is white player: " + white_player.get_player_name()

        elif num_black > num_white and self._players[0].get_player_color == "black":
            black_player = self._players[0]
            return "Winner is black player: " + black_player.get_player_name()

        elif num_black > num_white and self._players[1].get_player_color == "black":
            black_player = self._players[1]
            return "Winner is black player: " + black_player.get_player_name()

        elif num_black == num_white:
            "It's a tie"

    def make_move(self, color, piece_position):
        """Puts a piece of the specified color at the given position
        and updates the board accordingly, then returns the current board"""
        row = piece_position[0]
        column = piece_position[1]

        pot_captured = []
        self_piece, opposite_piece = ("X", "O") if color == "black" else ("O", "X")
        self._board[row][column] = self_piece

        if self_piece == "white":
            self._white_pieces += 1

        elif self_piece == "black":
            self._black_pieces += 1

        # check down
        temp = row
        while self._board[temp + 1][column] != self_piece:
            if self._board[temp + 1][column] == opposite_piece:
                pot_captured.append((temp + 1, column))
                temp += 1
                continue
            elif self._board[temp + 1][column] == "." or self._board[temp + 1][column] == "*":
                for trash in pot_captured:  # dump out these values
                    pot_captured.pop()
                break
            else:
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check up
        temp = row
        while self._board[temp - 1][column] != self_piece:
            if self._board[temp - 1][column] == opposite_piece:
                pot_captured.append((temp - 1, column))
                temp -= 1
                continue
            elif self._board[temp - 1][column] == "." or self._board[temp - 1][column] == "*":
                for trash in pot_captured:  # dump out these values
                    pot_captured.pop()  # takes that item out of the list
                break
            else:
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check left
        temp = column
        while self._board[row][temp - 1] != self_piece:
            if self._board[row][temp - 1] == opposite_piece:
                pot_captured.append((row, temp - 1))
                temp -= 1
                continue
            elif self._board[row][temp - 1] == "." or self._board[row][temp - 1] == "*":
                for trash in pot_captured:
                    pot_captured.pop()
                break
            else:
                # I think the pot_captured needs to be trashed here
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check right
        temp = column
        while self._board[row][temp + 1] != self_piece:
            if self._board[row][temp + 1] == opposite_piece:
                pot_captured.append((row, temp + 1))
                temp += 1
                continue
            elif self._board[row][temp + 1] == "." or self._board[row][temp + 1] == "*":
                for trash in pot_captured:
                    pot_captured.pop()
                break
            else:
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check top left
        temp_row = row
        temp_column = column
        while self._board[temp_row - 1][temp_column - 1] != self_piece:
            if self._board[temp_row - 1][temp_column - 1] == opposite_piece:
                pot_captured.append((temp_row - 1, temp_column - 1))
                temp_row -= 1
                temp_column -= 1
                continue
            elif self._board[temp_row - 1][temp_column - 1] == "." or self._board[temp_row - 1][temp_column - 1] == "*":
                for trash in pot_captured:
                    pot_captured.pop()
                break
            else:
                continue

        # if pot_captured makes it out of the while loop
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check top right
        temp_row = row
        temp_column = column
        while self._board[temp_row - 1][temp_column + 1] != self_piece:
            if self._board[temp_row - 1][temp_column + 1] == opposite_piece:
                pot_captured.append((temp_row - 1, temp_column + 1))
                temp_row -= 1
                temp_column += 1
                continue
            elif self._board[temp_row - 1][temp_column + 1] == "." or self._board[temp_row - 1][temp_column + 1] == "*":
                for trash in pot_captured:
                    pot_captured.pop()
                break
            else:
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check bottom right
        temp_row = row
        temp_column = column

        while self._board[temp_row + 1][temp_column + 1] != self_piece:
            if self._board[temp_row + 1][temp_column + 1] == opposite_piece:
                pot_captured.append((temp_row + 1, temp_column + 1))
                temp_row += 1
                temp_column += 1
                continue
            elif self._board[temp_row + 1][temp_column + 1] == "." or self._board[temp_row + 1][temp_column + 1] == "*":
                for trash in pot_captured:
                    pot_captured.pop()
                break
            else:
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        # check bottom left
        temp_row = row
        temp_column = column
        while self._board[temp_row + 1][temp_column - 1] != self_piece:
            if self._board[temp_row + 1][temp_column - 1] == opposite_piece:
                pot_captured.append((temp_row + 1, temp_column - 1))
                temp_row += 1
                temp_column -= 1
                continue
            elif self._board[temp_row + 1][temp_column - 1] == "." or self._board[temp_row + 1][temp_column - 1] == "*":
                for trash in pot_captured:
                    pot_captured.pop()
                break
            else:
                continue

        # if pot_captured actually makes it out of the while loop, then there's pieces to capture
        if len(pot_captured) > 0:
            for index, pieces in enumerate(pot_captured):
                new_row = pieces[0]
                new_column = pieces[1]
                self._board[new_row][new_column] = self_piece
                if self_piece == "white":
                    self._white_pieces += 1

                elif self_piece == "black":
                    self._black_pieces += 1

        pot_captured.clear()
        return self._board

    def play_game(self, player_color, piece_position):
        """Attempts to make a move for the player with the given color at the specified position"""

        valid_moves = self.return_available_positions(player_color)
        print("Here are the valid moves:", valid_moves)
        row = piece_position[0]
        column = piece_position[1]
        white_valid_moves = self.return_available_positions("white")
        black_valid_moves = self.return_available_positions("black")

        # checking if the move is valid
        if player_color == "white":
            if piece_position not in white_valid_moves:
                return "Invalid move"

        if player_color == "black":
            if piece_position not in black_valid_moves:
                return "Invalid move"

        if len(valid_moves) == 0 or self._board[row][column] == "*":
            return "Invalid move"

        if row is None or column is None:
            return "Invalid move"

        self.make_move(player_color, piece_position)

        # looking at what the next set of valid moves are
        white_valid_moves = self.return_available_positions("white")
        black_valid_moves = self.return_available_positions("black")

        # Seeing if the game is over
        if len(white_valid_moves) == 0 and len(black_valid_moves) == 0:
            dont_say_anything = self.return_winner()
            print("Game is ended white piece: " + str(self._white_pieces) + " black piece: " + str(self._black_pieces))
            return self.return_winner()

        return


print("Othello is a 2-player strategy board game with two players (Black and White)."
      "You will go first as the Black player.\n"
      "To begin playing the game, run run_game in main function.\n")


