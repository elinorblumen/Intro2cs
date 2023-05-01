#####################################################################################################
# File : asteroids_main
# Writer : ElinorB
# Exercise : ex8
# Description : Program for running 'Asteroids' game
#####################################################################################################
#Imports
#####################################################################################################

from screen import Screen
import sys
import ship
import asteroid
import random
import math
import torpedo

#####################################################################################################
#Constants
#####################################################################################################

DEFAULT_ASTEROIDS_NUM = 5
X_AXIS_MIN = -500
X_AXIS_MAX = 500
Y_AXIS_MIN = -500
Y_AXIS_MAX = 500
X_DELTA_AXIS = X_AXIS_MAX-X_AXIS_MIN
Y_DELTA_AXIS = Y_AXIS_MAX-Y_AXIS_MIN
CHANGE_DIR = 7
PIE_DEG = 180
ONE_LIFE_DROP = 1
ACCEL_FACTOR = 2
START_SCORE = 0
ASTEROID_S = (1,2,3)
SCORE = (100, 50, 20)
ONE = 1
MAX_LIFE = 200
MAX_TORPEDOS = 15
ZERO = 0

#####################################################################################################
#Class GameRunner
#####################################################################################################


class GameRunner:

    def __init__(self, asteroids_amnt=3):
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self._ship = ship.Ship(self.random_location()[0], self.random_location()[1])
        self._asteroids = []
        self._torpedos = []
        for i in range(asteroids_amnt):
            temp_asteroid = asteroid.Asteroid(self.asteroid_random_location()[0],
                                              self.asteroid_random_location()[1],
                                              self.random_speed()[0],self.random_speed()[1])
            self._asteroids.append(temp_asteroid)
            self._screen.register_asteroid(temp_asteroid, temp_asteroid.get_size())
        self._score = START_SCORE


    def run(self):
        self._do_loop()
        self._screen.start_screen()


    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)


    def _game_loop(self):
        """
        Main method that runs all procedures.
        """

        self._ship.draw_ship(self._screen)

        for an_asteroid in self._asteroids:
            an_asteroid.draw_asteroid(self._screen)

        self.change_direction()
        self.speed_up()
        self.object_movement(self._ship)
        self._screen.set_score(self._score)

        for an_asteroid in self._asteroids:
            self.object_movement(an_asteroid)
            if an_asteroid.has_intersection(self._ship):
                self.life_dropper()
                self._screen.unregister_asteroid(an_asteroid)
                self._asteroids.remove(an_asteroid)

        if self._screen.is_space_pressed():
            if len(self._torpedos) <= MAX_TORPEDOS:
                self.torpedo_adding()

        if len(self._torpedos) > ZERO:
            for temp_torpedo in self._torpedos:
                temp_torpedo.set_life_time(ONE)
                self.torpedo_max_life_time(temp_torpedo)

        if len(self._torpedos) > ZERO:
            for temp_torpedo in self._torpedos:
                self.object_movement(temp_torpedo)
                temp_x = temp_torpedo.get_location()[0]
                temp_y = temp_torpedo.get_location()[1]
                temp_direction = temp_torpedo.get_direction()
                self._screen.draw_torpedo(temp_torpedo, temp_x,
                                          temp_y, temp_direction)

                for an_asteroid in self._asteroids:
                    if an_asteroid.has_intersection(temp_torpedo):

                        if an_asteroid.get_size() == ASTEROID_S[0]:
                            self._score += SCORE[0]

                        elif an_asteroid.get_size() == ASTEROID_S[1]:
                            self._score += SCORE[1]
                            self.asteroid_explosion(an_asteroid, temp_torpedo)

                        else:
                            self._score += SCORE[2]
                            self.asteroid_explosion(an_asteroid, temp_torpedo)

                        self._screen.unregister_asteroid(an_asteroid)
                        self._asteroids.remove(an_asteroid)
                        self._screen.unregister_torpedo(temp_torpedo)
                        self._torpedos.remove(temp_torpedo)

        if len(self._asteroids) == 0:
            self._screen.show_message('YOU WON!', 'No asteroids left')
            self._screen.end_game()
            sys.exit()

        if self._ship.life == 0:
            self._screen.show_message('GAME OVER', 'You missed all your chances')
            self._screen.end_game()
            sys.exit()

        if self._screen.should_end():
            self._screen.show_message('End game?', 'Are you sure you want to leave?')
            self._screen.end_game()
            sys.exit()

    def object_movement(self, object):
        """
        Method changes object location
        :param object: Object of type ship/ asteroid
        :return:
        """

        old_x_coord = object.get_location()[0]
        old_y_coord = object.get_location()[1]

        object_speed = object.get_speed()
        new_x_coord = (object_speed[0] + old_x_coord - X_AXIS_MIN)%X_DELTA_AXIS+X_AXIS_MIN
        new_y_coord = (object_speed[1]+old_y_coord-Y_AXIS_MIN)%Y_DELTA_AXIS+Y_AXIS_MIN

        object.set_location(new_x_coord, new_y_coord)


    def random_location(self):
        """
        Method generates random location on the screen given in x, y coordinates.
        Set a random location on the screen to ship.
        """

        x_axis = random.randint(X_AXIS_MIN, X_AXIS_MAX)
        y_axis = random.randint(X_AXIS_MIN, X_AXIS_MAX)

        return x_axis, y_axis


    def asteroid_random_location(self):
        """
        Method generates random location on the screen given in x, y coordinates.
        Set a random location on the screen to ship.
        """

        x_axis = random.randint(X_AXIS_MIN, X_AXIS_MAX)
        y_axis = random.randint(X_AXIS_MIN, X_AXIS_MAX)

        if x_axis != self._ship.get_location()[0] and\
                y_axis != self._ship.get_location()[1]:
            return x_axis, y_axis

        else:
            self.asteroid_random_location()


    def change_direction(self):
        """
        Method changes ship direction with respect to player pressing keys.
        Player pressing left key will result with ship angel changing in +7 deg.
        Player pressing right key will result with ship angel changing in -7 deg.
        """

        while self._screen.is_left_pressed():
            self._ship.set_ship_angle(CHANGE_DIR)

        while self._screen.is_right_pressed():
            self._ship.set_ship_angle(-CHANGE_DIR)


    def speed_up(self):
        """
        Method changes ship speed with respect to player pressing keys.
        While player presses up key ship speed will rise.
        """

        x_current_speed = self._ship.get_speed()[0]
        y_current_speed = self._ship.get_speed()[1]

        x_new_speed = x_current_speed+math.cos(self._ship.get_direction()*(math.pi/PIE_DEG))
        y_new_speed = y_current_speed+math.sin(self._ship.get_direction()*(math.pi/PIE_DEG))

        while self._screen.is_up_pressed():
            self._ship.set_speed(x_new_speed, y_new_speed)


    def random_speed(self):
        """
        Method generates random speed in x,y axis terms
        :return: Tuple representing x axis speed and y axis speed respectively
        """

        rand_deg = random.randint(0,360)
        rand_speed = random.randint(1, 10)
        x_speed = rand_speed+math.cos(rand_deg*(math.pi/PIE_DEG))
        y_speed = rand_speed+math.sin(rand_deg*(math.pi/PIE_DEG))

        return x_speed, y_speed

    def life_dropper(self):
        """
        When ship hits an asteroid function responsible for dropping ship's life by 1,
        printing a warning message on screen and updating remaining life on screen display.
        """

        self._ship.life -= ONE_LIFE_DROP
        self._screen.show_message('Be careful!', 'You lost one life point')
        self._screen.remove_life()


    def torpedo_adding(self):
        """
        Method for adding torpedo object
        """


        x_axis = self._ship.get_location()[0]
        y_axis = self._ship.get_location()[1]

        x_speed = self._ship.get_speed()[0]+ACCEL_FACTOR*math.cos(self._ship.get_direction()*(math.pi/PIE_DEG))
        y_speed = self._ship.get_speed()[1]+ACCEL_FACTOR*math.sin(self._ship.get_direction()*(math.pi/PIE_DEG))

        direction = self._ship.get_direction()

        temp_torpedo = torpedo.Torpedo(x_axis, y_axis, x_speed, y_speed, direction)

        self._torpedos.append(temp_torpedo)
        self._screen.register_torpedo(temp_torpedo)


    def asteroid_explosion(self, temp_asteroid, temp_torpedo):
        """
        Method for exploding an asteroid with size bigger than 1
        :param temp_asteroid: Exploding asteroid
        :param temp_torpedo: Hitting torpedo
        """

        x_axis = temp_asteroid.get_location()[0]
        y_axis = temp_asteroid.get_location()[1]

        x_speed = (temp_torpedo.get_speed()[0]+temp_asteroid.get_speed()[0])/math.sqrt\
            (temp_asteroid.get_speed()[0]**2+temp_asteroid.get_speed()[1]**2)
        y_speed = (temp_torpedo.get_speed()[1] + temp_asteroid.get_speed()[1]) / math.sqrt \
            (temp_asteroid.get_speed()[0] ** 2 + temp_asteroid.get_speed()[1] ** 2)

        size = temp_asteroid.get_size()

        temp_asteroid_1 = asteroid.Asteroid(x_axis, y_axis, x_speed, y_speed, size - ONE)

        self._asteroids.append(temp_asteroid_1)
        self._screen.register_asteroid(temp_asteroid_1, temp_asteroid_1.get_size())

        temp_asteroid_2 = asteroid.Asteroid(x_axis, y_axis, -ONE * x_speed, - ONE * y_speed, size - ONE)

        self._asteroids.append(temp_asteroid_2)
        self._screen.register_asteroid(temp_asteroid_2, temp_asteroid_2.get_size())


    def torpedo_max_life_time(self, temp_torpedo):
        """
        Method checks whether torpedo had reached its max lif time span
        and if it does, removes torpedo
        :param temp_torpedo: torpedo
        """

        if temp_torpedo.get_life_time() >= MAX_LIFE:
            self._screen.unregister_torpedo(temp_torpedo)
            self._torpedos.remove(temp_torpedo)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
