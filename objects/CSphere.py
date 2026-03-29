from vpython import *
from .Object import Object
from collider import JosiahSparkleCollider

# define Sphere object
class CSphere(Object):
    def __init__(self, rad, mass, position, col, velocity=vector(0, 0, 0)):

        super().__init__(mass, position, col, velocity)
        # add the sphere to
        JosiahSparkleCollider.add_object(self)

        self.radius = rad
        self.shape = sphere(pos=position, radius=rad, color=col)

        self.norm = vector(0, 0, 0)
        self.contact_point = vector(0, 0, 0)

        self.interval = [position.x - rad, position.x + rad]

    def collision(self):
        # handle collision with ground
        if self.pos.y - self.radius <= -5:
            self.pos.y = -5 + self.radius
            self.shape.y = -5 + self.radius

            self.norm = -self.grav()
            self.contact_point = self.pos - vector(0, self.radius, 0)

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

        self.interval[0] = self.pos.x - self.radius
        self.interval[1] = self.pos.x + self.radius

    def is_box(self) -> bool:
        return False

    def is_sphere(self) -> bool:
        return True

