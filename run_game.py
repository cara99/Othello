# Defines a program that allows the user, a Black player, to actually play against the computer

from Othello import *


def auto(name, game):
    game.create_player(name, "black")
    game.create_player("Computer", "white")
    decision = ""

    while decision.lower() != "quit":
        print("\n" + name + "\'s turn")
        game.print_board()
        print("\nHere are the valid moves:", game.return_available_positions("black"))

        decision = input("\nEnter a move or type quit to end game. \nThe move "
                         "should be in x,y form. If no valid moves, type pass: ")

        if len(game.return_available_positions("black")) == 0:
            print("\n" + name + " is out of moves")
        else:
            piece_position = tuple(int(num) for num in decision.split(","))

            valid_moves = game.return_available_positions("black")

            row = piece_position[0]
            column = piece_position[1]
            black_valid_moves = game.return_available_positions("black")

            if piece_position not in black_valid_moves:
                print("Invalid move")
                continue
            board = game.get_board()
            if len(valid_moves) == 0 or board[row][column] == "*":
                print("Invalid move")
                continue

            if row is None or column is None:
                print("Invalid move")
                continue

            game.make_move("black", piece_position)
            game.print_board()

        print("Now computer's turn")
        white_moves = game.return_available_positions("white")
        if len(white_moves) == 0:
            print("\nComputer is out of moves")
        else:
            white_move = white_moves[0]  # just chooses the first one
            # ideally this index would be random range from 0 to len(white_move)-1
            game.make_move("white", white_move)
            game.print_board()

        if len(white_moves) ==0 and len(black_valid_moves) == 0:
            dont_say_anything = game.return_winner()
            print("Game is ended white piece: " + str(board.get_white_pieces()) + " black piece: " +
                  str(board.get_black_pieces()))
            return game.return_winner()


def main():
    game = Othello()
    print("Othello is a 2-player strategy board game with two players (black and white) on an 8x8 board"
          "\nTo begin playing the game, run run_game in main function.\n")
    name = input('What is your name?\n')
    print(name + ",you will go first. You play as black (x) and the computer is playing as white (O)")
    auto(name, game)


if __name__ == "__main__":
    main()
