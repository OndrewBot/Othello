# Author: Andrew Bottom
# GitHub username: OndrewBot
# Date: 6/6/2023
# Description: This program simulates the game Othello. After a game is created, players can be
#           added to the game with the color of their choice (black or white). The players can
#           make moves and will be warned if the moves they make are invalid; they will be
#           supplied a list of possible moves in this case. The game is finished when no more
#           valid moves are available. The score will then be shown and the winner declared...
#           unless it's a tie.


class Player:
    """
    This class represents a player in the game Othello. It is created through
    Othello.create_player(player_name, color).
    Each Player object has a name and color (either black or white) that are passed
    as arguments. Each player has a number of pieces that's initialized as 2, which
    represent the two starting positions.
    """
    def __init__(self, color, name):
        self._color = color
        self._name = name
        self._pieces = 2  # every Player starts with 2 pieces

    def get_name(self):
        """
        Returns the name associated with a Player object.
        :return: player's name
        """
        return self._name

    def get_pieces(self):
        """
        Access and returns the number of pieces a Player object has
        :return: number of pieces of the Player object.
        """
        return self._pieces

    def change_pieces(self, number):
        """
        Adds or subtracts the number of pieces a player has based on the Othello game play.
        :param number: A positive or negative number
        :return: None
        """
        self._pieces += number


class Othello:
    """
    This class begins, controls, and ends a game of Othello, following the classic rules. This
    class's responsibilities are:
        Printing the board with the current piece positions.
        Creating a Player object, one white and one black.
        Determining the winner - declared when there are no more valid moves. The winner has
            the most pieces, or else it's a tie.
        Showing the available positions a Player can move to.
        Making a move and updating the board accordingly.
        Telling the player if they're making an invalid move or telling them there are no more valid moves.
    """
    def __init__(self):
        self._board = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', 'O', 'X', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', 'X', 'O', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*'],
                       ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self._players = {}
        self._positions = {
            'black': [(4, 5), (5, 4)],
            'white': [(4, 4), (5, 5)]
        }

    def print_board(self):
        """
        Shows the board with the current position of all the pieces.
        :return: The board, printed as a string, formatted with new lines
        """
        the_board = ''
        count = 0
        # join each row and add a \n
        for row in self._board:
            count += 1
            if count == len(self._board):  # the last row does not print \n
                row = ' '.join(row)
                the_board = the_board + row
            else:
                row = ' '.join(row)
                the_board = the_board + row + '\n'

        return print(the_board)

    def create_player(self, player_name, color):
        """
        Creates an object in the Player class.
        :param player_name: User's choice of name
        :param color: Color of the Player object's pieces, either 'black' or 'white'
        :return: None
        """
        player = Player(color, player_name)
        self._players[color] = player

    def return_winner(self):
        """
        Returns a statement regarding the winning player based on who has more
        pieces in their color when the game is over i.e., there are no more
        invalid moves.
        This is an internal method that's called by self.play_game().
        :return: Either "Winner is white player: player’s name", Winner is black
                player: player’s name", or "It's a tie"
        """
        black_score = self._players['black'].get_pieces()
        white_score = self._players['white'].get_pieces()
        if black_score == white_score:
            return "It's a tie"
        elif black_score > white_score:
            return "Winner is black player: " + self._players['black'].get_name()
        else:
            return "Winner is white player: " + self._players['white'].get_name()

    def rec_available_positions(self, row, column, direction, opponent):
        """
        Recursively increments the row or column in the prescribed direction until either an
        empty space is encountered '.', which means it's a valid move, or a '*' or a piece of
        the same color is encountered, in which case it's an invalid move.
        :param row: the board[x] position of the opponents piece. Passed by return_available_positions
                    method
        :param column: the board[][x] position of the opponents piece. Passed by return_available_positions
                       method
        :param direction: any of the cardinal directions (north, south, east, west, northeast, southeast,
                        northwest, southwest). This lets the method know whether to increment or decrement
                        either the row, the column, or both.
        :param opponent: This is the color of the opponents piece. The algorithm will continue moving
                        in the defined direction while this color is in the position.
        :return: If no valid positions are found, an empty list [] is returned.
                 If the position is valid, those coordinates are returned in a [list].
        """
        # base cases:
        if self._board[row][column] == '.':  # empty space encountered, list filled
            return row, column
        if self._board[row][column] == '*':  # boundary encountered, not valid
            return
        if opponent == 'black':
            if self._board[row][column] == 'O':  # if same piece is encountered, not valid
                return
        if opponent == 'white':
            if self._board[row][column] == 'X':  # if same piece is encountered, not valid
                return

        if direction == 'north':
            return self.rec_available_positions(row - 1, column, 'north', opponent)
        if direction == 'south':
            return self.rec_available_positions(row + 1, column, 'south', opponent)
        if direction == 'east':
            return self.rec_available_positions(row, column + 1, 'east', opponent)
        if direction == 'west':
            return self.rec_available_positions(row, column - 1, 'west', opponent)
        if direction == 'northeast':
            return self.rec_available_positions(row - 1, column + 1, 'northeast', opponent)
        if direction == 'northwest':
            return self.rec_available_positions(row - 1, column - 1, 'northwest', opponent)
        if direction == 'southeast':
            return self.rec_available_positions(row + 1, column + 1, 'southeast', opponent)
        if direction == 'southwest':
            return self.rec_available_positions(row + 1, column - 1, 'southwest', opponent)

    def return_available_positions(self, color):
        """
        Finds and returns a list of all available position for a Player of a specific
        color to move.
        This can be called by the User or by self.play_game().
        :param color: color of a Player object's pieces.
        :return: List of valid positions for a Player color pieces to move.
                List is empty if there are no valid moves.
        """
        opponent = 'white' if color == 'black' else 'black'

        positions_list = []
        for pos in self._positions[color]:  # each position for a player may have possible moves
            row = pos[0]
            column = pos[1]
            for opp_pos in self._positions[opponent]:  # possible moves are based on positions of opponent's pieces
                opp_row = opp_pos[0]
                opp_column = opp_pos[1]
                # horizontal movement check
                if opp_row == row and opp_column - column == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'east', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                elif opp_row == row and column - opp_column == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'west', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                # vertical movement check
                elif opp_column == column and opp_row - row == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'south', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                elif opp_column == column and row - opp_row == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'north', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                # diagonal movement check
                elif opp_column - column == 1 and opp_row - row == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'southeast', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                elif opp_column - column == 1 and row - opp_row == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'northeast', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                elif column - opp_column == 1 and opp_row - row == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'southwest', opponent)
                    positions_list.append(possible_positions) if possible_positions else []
                elif column - opp_column == 1 and row - opp_row == 1:
                    possible_positions = self.rec_available_positions(opp_row, opp_column, 'northwest', opponent)
                    positions_list.append(possible_positions) if possible_positions else []

        return positions_list

    def rec_make_move(self, opp_row, opp_column, direction, opponent, pieces_list=None):
        """
        Recursively increments the row or column in the prescribed direction until either a
        piece of the same color is encountered '.', which means it's a valid move, or a '*' or a piece of
        the opposite color is encountered, in which case it's an invalid move.
        :param opp_row: starting position for the opponent's piece
        :param opp_column: starting positions for the opponent's piece
        :param direction: any of the cardinal directions (north, south, east, west, northeast, southeast,
                        northwest, southwest). This lets the method know whether to increment or decrement
                        either the row, the column, or both.
        :param opponent: this is the opponent's color; this color is "followed" in the prescribed direction
                        until a base case is met
        :param pieces_list: this is a list of positions that will be changed via make_move method
        :return: None if invalid base case is met. pieces_list if valid base case met.
        """
        mark = 'X' if opponent == 'white' else 'O'

        if pieces_list is None:
            pieces_list = []

        # base cases:
        if self._board[opp_row][opp_column] == '.':  # empty space encountered, not valid
            return
        elif self._board[opp_row][opp_column] == '*':  # boundary encountered, not valid
            return
        elif self._board[opp_row][opp_column] == mark:  # if same piece is encountered, valid and added to the list
            return pieces_list
        else:
            pieces_list.append((opp_row, opp_column))  # add the current piece position
            # continues recursively while the position holds the opponent's mark
            if direction == 'north':
                return self.rec_make_move(opp_row - 1, opp_column, 'north', opponent, pieces_list)
            if direction == 'south':
                return self.rec_make_move(opp_row + 1, opp_column, 'south', opponent, pieces_list)
            if direction == 'east':
                return self.rec_make_move(opp_row, opp_column + 1, 'east', opponent, pieces_list)
            if direction == 'west':
                return self.rec_make_move(opp_row, opp_column - 1, 'west', opponent, pieces_list)
            if direction == 'northeast':
                return self.rec_make_move(opp_row - 1, opp_column + 1, 'northeast', opponent, pieces_list)
            if direction == 'northwest':
                return self.rec_make_move(opp_row - 1, opp_column - 1, 'northwest', opponent, pieces_list)
            if direction == 'southeast':
                return self.rec_make_move(opp_row + 1, opp_column + 1, 'southeast', opponent, pieces_list)
            if direction == 'southwest':
                return self.rec_make_move(opp_row + 1, opp_column - 1, 'southwest', opponent, pieces_list)

    def make_move(self, color, piece_position):
        """
        Allows a new color to be placed on the board (X-black, O-white). After the move
        is made, any pieces of the other color that are between it and another of the
        moved color's pieces are "taken" i.e., changed to the other color. The pieces
        that are between must be in a line - horizontal, vertical, or diagonal.
        This is an internal method that is called by self.play_game().
        :param color: color of the Player object's piece that is making the move
        :param piece_position: destination position (validity not checked)
        :return: the current board as a 2D list
        """
        # get info for the player and their opponent
        opponent = 'black' if color == 'white' else 'white'
        mark = 'O' if color == 'white' else 'X'
        # since position has already been validated:
        #   add the initial mark to the board, the position of their piece to the list, and increment number of pieces
        row = piece_position[0]
        column = piece_position[1]
        self._board[row][column] = mark
        self._positions[color].append(piece_position)
        self._players[color].change_pieces(1)

        taken_pieces_list = []      # holds all the piece positions to be converted to the other color
        for opp_pos in self._positions[opponent]:  # each opponent position is compared to argument position
            opp_row = opp_pos[0]
            opp_column = opp_pos[1]
            # horizontal movement check
            if opp_row == row and opp_column - column == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'east', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            elif opp_row == row and column - opp_column == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'west', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            # vertical movement check
            elif opp_column == column and opp_row - row == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'south', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            elif opp_column == column and row - opp_row == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'north', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            # diagonal movement check
            elif opp_column - column == 1 and opp_row - row == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'southeast', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            elif opp_column - column == 1 and row - opp_row == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'northeast', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            elif column - opp_column == 1 and opp_row - row == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'southwest', opponent)
                taken_pieces_list += possible_positions if possible_positions else []
            elif column - opp_column == 1 and row - opp_row == 1:
                possible_positions = self.rec_make_move(opp_row, opp_column, 'northwest', opponent)
                taken_pieces_list += possible_positions if possible_positions else []

        for pos in taken_pieces_list:   # complete the move by transferring all marks/positions
            row = pos[0]
            column = pos[1]
            self._board[row][column] = mark
            self._positions[color].append(pos)
            self._positions[opponent].remove(pos)
            self._players[color].change_pieces(1)
            self._players[opponent].change_pieces(-1)
        return self._board

    def play_game(self, player_color, piece_position):
        """
        The user picks a color and position and submits it to the Othello object as the
        corresponding Player object's move.
        This method checks the validity of a move and returns an invalid move string as
        well as printing a message that shows the valid moves via self._return_valid_positions().
        If no valid moves are available, the valid move message shows an empty list.
        Valid moves will update the board and make the move via self.make_move().
        If the last valid move was made, then the scores will be displayed and
        self.return_winner() will be called.
        :param player_color: Color of the piece being moved
        :param piece_position: Destination position of the piece
        :return: "Invalid move" if invalid move was made. Prints valid moves in this case.
                 Valid moves return None.
                 "Game is ended white piece: number black piece: number" if game is over and
                 returns self.return_winner() via call as well.
        """

        opponent = 'black' if player_color == 'white' else 'white'  # define player color variables
        # check if move was valid
        available_positions = self.return_available_positions(player_color)
        if piece_position in available_positions:
            # pass to make_move method
            self.make_move(player_color, piece_position)
            # check if either black or white have valid moves remaining
            if (self.return_available_positions(player_color) == [] and
                    self.return_available_positions(opponent) == []):
                # tally scores and end game
                white_score = self._players['white'].get_pieces()
                black_score = self._players['black'].get_pieces()
                print(f'Game is ended white piece: {white_score} black piece: {black_score}')
                return self.return_winner()
        else:   # invalid move selected
            print(f'Here are the valid moves: {self.return_available_positions(player_color)}.')
            return "Invalid move"
