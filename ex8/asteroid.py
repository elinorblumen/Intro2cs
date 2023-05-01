#######################################################################################
#Imports
#######################################################################################

import math

#######################################################################################
#Constants
#######################################################################################

RADIUS_SIZE_COEF = 10
RADIUS_NORMA_COEF = 5

#######################################################################################
#Class Asteroids
#######################################################################################


class Asteroid:
    """
    A class defining asteroid object and all its methods.
    """

    def __init__(self, x_axis, y_axis, x_speed=0, y_speed=0, size=3):
        """
        The initiator for asteroid.
        :param x_axis: Float number representing x axis location
        :param y_axis: Float number representing y axis location
        :param x_speed: Float number representing x axis speed
        :param y_speed: Float number representing y axis speed
        :param size: Integer within range (1,3)
        """

        self._x_axis = x_axis
        self._y_axis = y_axis
        self._x_speed = x_speed
        self._y_speed = y_speed
        self._size = size


    def draw_asteroid(self, screen):
        """
        A method meant to draw asteroid to screen with given location.
        :param screen: A screen object
        """

        screen.draw_asteroid(self, self._x_axis, self._y_axis)


    def set_location(self, x_axis, y_axis):
        """
        Setter method to set new location
        :param x_axis: X axis coordinate, in range (-500,500)
        :param y_axis: Y axis coordinate, in range (-500,500)
        """

        self._x_axis = x_axis
        self._y_axis = y_axis


    def set_speed(self, x_speed, y_speed):
        """
        Setter method to set new speed
        :param x_speed: X axis speed
        :param y_speed: Y axis speed
        """

        self._x_speed = x_speed
        self._y_speed = y_speed


    def get_location(self):
        """
        Getter method for asteroid loction
        :return: x, y coordinates tuple
        """

        return self._x_axis, self._y_axis


    def get_speed(self):
        """
        Getter method for asteroid speed
        :return: Tuple with x axis speed and y axis speed respectively
        """

        return self._x_speed, self._y_speed


    def get_size(self):
        """
        Getter method for asteroid size
        :return: Integer in range (1,3) representing asteroid size
        """

        return self._size

    def has_intersection(self, obj):
        """
        Method checks if asteroid has intersection with other object
        :param obj: Torpedo or ship
        :return: True if there's an intersection, False otherwise
        """

        object_location = obj.get_location()

        temp_distance = math.sqrt((object_location[0]-self._x_axis)**2 +
                                  (object_location[1]-self._y_axis)**2)

        radius = self.asteroid_radius()

        if temp_distance <= radius + obj.radius:
            return True

        else:
            return False


    def asteroid_radius(self):
        """
        Method defining radius for asteroid
        :return: Asteroid radius
        """

        return self._size*RADIUS_SIZE_COEF-RADIUS_NORMA_COEF
