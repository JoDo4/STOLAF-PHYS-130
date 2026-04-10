import pygame
from .Object import Object
from collision_pygame.collider2 import Collision

# define Sphere object
class CSphere(Object):
    def __init__(self, rad : int = 1, mass : int = 1, position = pygame.Vector2(0,0), color : str = "white", velocity=pygame.Vector2(0, 0)):

        super().__init__(mass, position, color, velocity)
        # add the sphere to
        Collision.add_object(self)

        self.radius = rad


        self.norm = pygame.Vector2(0, 0)
        self.contact_point = pygame.Vector2(0, 0)

        self.interval = [position.x - rad, position.x + rad]

    def update_p(self, dt, f_total = 0):
        if f_total == 0:
            f_total = self.grav() + self.norm
        self.p += f_total * dt

    def update_v(self):
        self.v = self.p / self.m

    def update_pos(self, dt):
        self.pos += self.v * dt

        self.interval[0] = self.pos.x - self.radius
        self.interval[1] = self.pos.x + self.radius

    def is_box(self) -> bool:
        return False

    def is_sphere(self) -> bool:
        return True

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, color= self.color, radius = self.radius, center = self.pos)


