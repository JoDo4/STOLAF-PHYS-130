from vpython import *

# create our parent class
class Object:
    def __init__(self, mass, position, col, velocity=vector(0, 0, 0)):
        self.m = mass
        self.pos = position
        self.v = velocity
        self.p = velocity * mass

        self.color = col

    def collision(self):
        # function to detect if anything is hitting the object
        pass

    def grav(self):
        # function to determine force of gravity on object
        return vector(0, -self.m * 9.8, 0)

    def update_p(self, dt):
        pass

    def update_v(self):
        pass

    def update_pos(self, dt):
        pass
