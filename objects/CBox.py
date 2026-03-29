from vpython import *
from .Object import Object
from collider import JosiahSparkleCollider

# define the Box object
class CBox(Object):

    def __init__(self, length=1, height=1, width=1, mass=1, position=vector(0, 0, 0), color = color.white,
                 velocity=vector(0, 0, 0), axis=vector(0, 0, 0)):

        super().__init__(mass, position, color, velocity)

        # add itself to the object list
        JosiahSparkleCollider.add_object(self)

        self.length = length
        self.height = height
        self.width = width
        self.axis = axis
        self.shape = box(pos=position, color=color, axis=axis, length=length, height=height, width=width)

        self.norm = vector(0, 0, 0)
        self.contact_point = vector(0, 0, 0)

        self.interval = [position.x - length / 2, position.x + length / 2]

    def collision(self):
        if self.pos.y - self.height / 2 <= -5:
            self.pos.y = -5 + self.height / 2
            self.shape.y = -5 + self.height / 2

            self.norm = -self.grav()
            self.contact_point = self.pos - vector(0, self.length / 2, 0)

            self.v.y = 0
            self.p.y = 0
        # if sphere is not on ground
        else:
            self.norm = vector(0, 0, 0)
            self.contact_point = vector(0, 0, 0)

    def update_p(self, dt):
        F_total = self.grav() + self.norm
        self.p += F_total * dt

    def update_v(self):
        self.v = self.p / self.m

    def update_pos(self, dt):
        self.pos += self.v * dt
        self.shape.pos += self.v * dt

        self.interval[0] = self.pos.x - self.length / 2
        self.interval[1] = self.pos.x + self.length / 2

    def is_box(self)-> bool:
        return True

    def is_sphere(self)->bool:
        return False



