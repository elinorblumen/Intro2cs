############################################################
# Imports
############################################################
from car import Car, Direction


############################################################
# Constants
############################################################

CAR_LENGTH = (2, 3, 4)
NOT_ADDED_MSG = 'Car was not added successfully.'
ADDED_MSG = 'Car was added successfully!'
LOCATION_NOT_FREE = 'New location is not free.'
EMPTY_LOCATION = '_'
NON_V_DIR = 'Non valid direction.'
VALID_DIRECTIONS = {3, 4, 5, 6}

############################################################
# Class definition
############################################################


class Board():
    """
    A class representing a rush hour board.
    """

    def __init__(self, cars, exit_board, size=6):
        """
        Initialize a new Board object.
        :param cars: A list (or dictionary) of cars.
        :param size: Size of board (Default size is 6). 
        """
        self.__cars = [car for car in cars]
        self.__exit_board = exit_board
        self.__size = size
        self.__board = {(x, y): EMPTY_LOCATION for x in range(self.__size) for y in range(self.__size)}
        for i in range(self.__size):
            self.__board[(-1, i)] = str(i)
            self.__board[(i, -1)] = str(i)
            self.__board[(self.__size, i)] = str(i)
            self.__board[(i, self.__size)] = str(i)
        self.__board[(-1, self.__size)] = '*'
        self.__board[(self.__size, -1)] = '*'
        self.__board[(self.__size, self.__size)] = '*'
        self.__board[(-1, -1)] = '*'
        self.__board[self.__exit_board] = 'E'


    def add_car(self, car):
        """
        Add a single car to the board.
        :param car: A car object
        :return: True if a car was successfully added, or False otherwise.
        """

        if self.is_empty(car.location):

            if car.orientation == Direction.VERTICAL:
                for i in range(1, 4):
                    location_span = (car.location[0]+i, car.location[1])
                    if car.length >= CAR_LENGTH[i - 1]:
                        if not self.is_empty(location_span):
                            print(NOT_ADDED_MSG)
                            return False
                    self.__board[location_span] = car.color
                    if car.length == CAR_LENGTH[i-1]:
                        self.__cars.append(car)
                        self.__board[car.location] = car.color
                        print(ADDED_MSG)
                        return True

            if car.orientation == Direction.HORIZONTAL:
                for i in range(1, car.length):
                    location_span = (car.location[0], car.location[1] + i)
                    if car.length >= CAR_LENGTH[i-1]:
                        if not self.is_empty(location_span):
                            print(NOT_ADDED_MSG)
                            return False
                    self.__board[location_span] = car.color
                    if car.length == CAR_LENGTH[i-1]:
                        self.__cars.append(car)
                        self.__board[car.location] = car.color
                        print(ADDED_MSG)
                        return True
        print(NOT_ADDED_MSG)
        return False


    def add_car_no_print(self, car):
        """
        Add a single car to the board.
        :param car: A car object
        :return: True if a car was successfully added, or False otherwise.
        """

        if self.is_empty(car.location):

            if car.orientation == Direction.VERTICAL:

                for i in range(1, 4):
                    location_span = (car.location[0]+i, car.location[1])
                    if car.length > CAR_LENGTH[i - 1]:
                        if not self.is_empty(location_span):
                            return False
                        self.__board[location_span] = car.color

                    if car.length == CAR_LENGTH[i-1]:
                        self.__board[location_span] = car.color
                        self.__cars.append(car)
                        self.__board[car.location] = car.color
                        return True

            if car.orientation == Direction.HORIZONTAL:
                for i in range(1, car.length):
                    location_span = (car.location[0], car.location[1] + i)
                    if car.length > CAR_LENGTH[i-1]:
                        if not self.is_empty(location_span):
                            return False
                        self.__board[location_span] = car.color

                    else:
                        if car.length == CAR_LENGTH[i-1]:
                            if not self.is_empty(location_span):
                                return False
                            self.__board[location_span] = str(car.color)
                            self.__cars.append(car)
                            self.__board[car.location] = str(car.color)
                            return True
        return False
    
    def is_empty(self, location):
        """
        Check if a given location on the board is free.
        :param location: x and y coordinations of location to be check
        :return: True if location is free, False otherwise
        """

        if not 0 <= location[0] < self.__size or not 0 <= location[1] < self.__size:
            return False

        for car in self.__cars:
            if location == car.location:
                return False
            if car.orientation == Direction.VERTICAL:
                for i in range(1, 4):
                    location_span = (car.location[0]+i, car.location[1])
                    if location == location_span:
                        if car.length >= CAR_LENGTH[i-1]:
                            return False

            if car.orientation == Direction.HORIZONTAL:
                for i in range(1, 4):
                    location_span = (car.location[0], car.location[1] + i)
                    if location == location_span:
                        if car.length >= CAR_LENGTH[i - 1]:
                            return False
        return True

    
    def move(self, car, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False otherwise.
        """

        if direction not in VALID_DIRECTIONS:
            print(NON_V_DIR)
            return False

        new_location = list(car.location)

        if direction == Direction.UP:
            if car.orientation == Direction.HORIZONTAL:
                print(NON_V_DIR)
                return False
            else:
                new_location[0] -= 1

        elif direction == Direction.DOWN:
            if car.orientation == Direction.HORIZONTAL:
                print(NON_V_DIR)
                return False
            else:
                new_location[0] += 1

        elif direction == Direction.RIGHT:
            if car.orientation == Direction.VERTICAL:
                print(NON_V_DIR)
                return False
            else:
                new_location[1] += 1

        elif direction == Direction.LEFT:
            if car.orientation == Direction.VERTICAL:
                print(NON_V_DIR)
                return False
            else:
                new_location[1] -= 1


        new_location = tuple(new_location)
        self.delete_car(car)
        temp_lst = []
        temp_lst.append(car)
        self.__cars.remove(car)


        if car.orientation == Direction.VERTICAL:

            for i in range(1, 4):
                if direction != Direction.DOWN and direction != Direction.UP:
                    print(NON_V_DIR)
                    return False
                if direction == Direction.DOWN:
                    location_span = (new_location[0]+i, new_location[1])
                if direction == Direction.UP:
                    location_span = (new_location[0], new_location[1])

                if car.length > CAR_LENGTH[i - 1]:
                    if not self.is_empty(location_span):
                        self.add_car_no_print(car)
                        print(LOCATION_NOT_FREE)
                        return False
                else:
                    if car.length == CAR_LENGTH[i-1]:
                        if not self.is_empty(location_span):
                            self.add_car_no_print(car)
                            print(LOCATION_NOT_FREE)
                            return False

                        else:
                            car.location = new_location
                            self.add_car_no_print(car)
                            return True


        if car.orientation == Direction.HORIZONTAL:

            for i in range(1, 4):

                if direction != Direction.RIGHT and direction != Direction.LEFT:
                    print(NON_V_DIR)
                    return False

                if direction == Direction.RIGHT:
                    location_span = (new_location[0], new_location[1]+i)
                if direction == Direction.LEFT:
                    location_span = (new_location[0], new_location[1])


                if car.length > CAR_LENGTH[i - 1]:
                    if not self.is_empty(location_span):
                        self.add_car_no_print(car)
                        print(LOCATION_NOT_FREE)
                        return False

                else:
                    if car.length == CAR_LENGTH[i-1]:

                        if not self.is_empty(location_span):
                            print(LOCATION_NOT_FREE)
                            self.add_car_no_print(car)
                            return False

                        else:
                            car.location = new_location
                            self.add_car_no_print(car)
                            return True

        else:
            return False



    def get_car(self):
        """
        'Getter' function to get the list of cars of an object from class Board
        :return: A list of object car, from class Car
        """

        return self.__cars


    def get_exit_board(self):
        """
        A 'getter' function meant to return the exit coordinates of an board object.
        """

        return self.__exit_board


    def get_size(self):
        """
        A 'getter' function meant to return the size of a board object.
        """

        return self.__size


    def add_car_to_list(self, car):
        """
        A 'setter' function meant to add a car to the list of cars of a board object.
        :param car: A car object from Car class.
        """


        return self.__cars.append(car)


    def get_dict_board(self):
        """
        A 'getter' function meant to return a dictionary representing the board object.
        :return: Dictionary of the board
        """

        return self.__board


    def delete_car(self, car):
        """
        A function meant to remove a car object coordinats from the board dictionary.
        yet, the function doesn't remove the car from the board object car list.
        :param car: A car to be removed
        """

        self.__board[car.location] = str('_')

        if car.orientation == Direction.VERTICAL:
            for i in range(1, 4):
                location_span = (car.location[0]+i, car.location[1])
                if car.length >= CAR_LENGTH[i - 1]:
                    self.__board[location_span] = str('_')
                    return True

        if car.orientation == Direction.HORIZONTAL:
            for i in range(1, car.length):
                location_span = (car.location[0], car.location[1] + i)
                if car.length >= CAR_LENGTH[i-1]:
                    self.__board[location_span] = str('_')
                    return True

        return False

    
    def __repr__(self):
        """
        :return: Return a string representation of the board.
        """

        board_str = ''

        for x in range(-1, self.__size + 1):
            for y in range(-1, self.__size + 1):
                board_str += " ' " + str(self.__board[(x, y)]) + " ' "
                if y == self.__size:
                    board_str += '\n'

        return board_str













