
#######################################################################################
#Constants
#######################################################################################

SHIP_RADIUS = 1
FULL_LIFE = 3

#######################################################################################
#Class ship
#######################################################################################


class Ship:
    """
    A class defining ship object and all its methods.
    """

    def __init__(self, x_axis, y_axis, x_speed=0, y_speed=0, direction=0):
        """
        The initiator for ship.
        :param x_axis: Float number representing x axis location
        :param y_axis: Float number representing y axis location
        :param x_speed: Float number representing x axis speed
        :param y_speed: Float number representing y axis speed
        :param direction: Float number representing direction in degrees
        """

        self._x_axis = x_axis
        self._y_axis = y_axis
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._direction = direction
        self.radius = SHIP_RADIUS
        self.life = FULL_LIFE


    def draw_ship(self, screen):
        """
        Method meant to draw ship to screen with given location and direction.
        :param screen: A screen object
        """

        screen.draw_ship(self._x_axis, self._y_axis, self._direction)


    def set_ship_angle(self, degrees):
        """
        Setter sets ship direction.
        :param degrees: dagrees to be added to ship's current direction
        """

        self._direction += degrees


    def set_location(self, x_axis, y_axis):
        """
        Setter to set new location
        :param x_axis: X axis coordinate, in range (-500,500)
        :param y_axis: Y axis coordinate, in range (-500,500)
        """

        self._x_axis = x_axis
        self._y_axis = y_axis


    def set_speed(self, x_speed, y_speed):
        """
        Setter to set new speed
        :param x_speed: X axis speed
        :param y_speed: Y axis speed
        """

        self._x_speed = x_speed
        self._y_speed = y_speed


    def get_location(self):
        """
        Getter for ship loction
        :return: x, y coordinates tuple
        """

        return self._x_axis, self._y_axis


    def get_speed(self):
        """
        Getter for ship speed
        :return: Tuple with x axis speed and y axis speed respectively
        """

        return self._x_speed, self._y_speed


    def get_direction(self):
        """
        Getter for ship direction
        :return: Direction in degrees
        """

        return self._direction





