############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction
from board import Board

############################################################
# Class definition
############################################################

SINGLE_TURN_ERROR = 'Unable to move car'
COLOR_MSG = 'Please enter color of car would you like to move. options are: y, b, o, g, p, w, r '
VALID_COLORS = {'y','b','o','g', 'p', 'w', 'r'}

class Game:
    """
    A class representing a rush hour game.
    A game is composed of cars that are located on a square board and a user
    which tries to move them in a way that will allow the red car to get out
    through the exit
    """

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Print board to the screen
            2. Get user's input of: what color car to move, and what direction to
                move it.
            2.a. Check the the input is valid. If not, print an error message and
                return to step 2.
            2. Move car according to user's input. If movement failed (trying
                to move out of board etc.), return to step 2.
            3. Report to the user the result of current round ()
        """

        print(self.__board)

        color_input = input(COLOR_MSG)

        while color_input not in VALID_COLORS:
            print(gh.ERROR_CAR_COLOR)
            color_input = input(COLOR_MSG)

        direction_input = gh.get_direction()

        for car in self.__board.get_car():
            if car.color == color_input:
                self.__board.move(car, direction_input)
                return True

        print(SINGLE_TURN_ERROR)
        return False


    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print('Welcome to Rush Hour game!')
        print(self.__board)

        exit_board = self.__board.get_exit_board()

        if exit_board[0] == -1 or self.__board.get_size()+2:
            car_r = Car('r', 2, (3, exit_board[1]), Direction.VERTICAL)
            self.__board.add_car_no_print(car_r)
            self.__board.add_car_to_list(car_r)

        elif exit_board[1] == -1 or self.__board.get_size()+2:
            car_r = Car('r', 2, (exit_board[0], 3), Direction.HORIZONTAL)
            self.__board.add_car_no_print(car_r)
            self.__board.add_car_to_list(car_r)

        num_cars = gh.get_num_cars()
        car_lst = []


        for i in range(num_cars):
            car_input = gh.get_car_input(self.__board.get_size())
            car_i = Car(car_input[0], car_input[1], car_input[2], car_input[3])
            car_lst.append(car_i)

        for car in car_lst:
            self.__board.add_car_no_print(car)
            self.__board.add_car_to_list(car)


        if car_r.orientation == Direction.VERTICAL:
            if exit_board[0] == -1:
                while board.get_dict_board()[car_r.location] != (exit_board[0]+1, exit_board[1]):
                    self.__single_turn()
                    continue
                else:
                    gh.report_game_over()

            if exit_board[0] == self.__board.get_size():
                while board.get_dict_board()[car_r.location] != (exit_board[0]-1, exit_board[1]):
                    self.__single_turn()
                    continue
                else:
                    gh.report_game_over()

        if car_r.orientation == Direction.HORIZONTAL:
            while exit_board[1] == -1:
                if board.get_dict_board()[car_r.location] != (exit_board[0], exit_board[1]+1):
                    self.__single_turn()
                    continue
                else:
                    gh.report_game_over()

            if exit_board[1] == self.__board.get_size()+1:
                while board.get_dict_board()[car_r.location] != (exit_board[0], exit_board[1]-1):
                    self.__single_turn()
                    continue
                else:
                    gh.report_game_over()







############################################################
# An example usage of the game
############################################################
if __name__=="__main__":

    board = Board([], (6, 3)) # if using a dictionry of cars. use '[]' if using a list
    game = Game(board)
    game.play()






