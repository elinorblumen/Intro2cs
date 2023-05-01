
#######################################################################################
#Constants
#######################################################################################

RADIUS_SIZE = 4
START = 0

#######################################################################################
#Class Asteroids
#######################################################################################





class Torpedo:

    def __init__(self, x_axis, y_axis, x_speed, y_speed, direction):

        self._x_axis = x_axis
        self._y_axis = y_axis
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._direction = direction
        self.radius = RADIUS_SIZE
        self._life_time = START



    def get_location(self):
        """
        Getter for location
        :return: x,y tuple of location
        """
        return self._x_axis, self._y_axis


    def get_speed(self):
        """
        Getter for speed
        :return: x,y tuple representing x axis speed and y axis speed
        """
        return self._x_speed, self._y_speed


    def get_direction(self):
        """
        Getter for torpedo direction
        :return: Direction in degrees
        """

        return self._direction

    def set_location(self, x_axis, y_axis):
        """
        Setter for setting torpedo location
        """

        self._x_axis = x_axis
        self._y_axis = y_axis

    def get_life_time(self):
        """
        Getter for torpedo life time
        :return: integer in range (1,200)
        """

        return self._life_time

    def set_life_time(self, int):
        """
        Setter for adding life time to current torpedo life time
        :param int: int
        """

        self._life_time += int

