import pygame
from .Object import Object
from collision_pygame.collider2 import Collision

# define the Box object
class CBox(Object):

    def __init__(self, length : int =1, height : int=1, mass : int =1,
                 position=pygame.Vector2(0, 0), color : str = "white",
                 velocity=pygame.Vector2(0, 0)):

        super().__init__(mass, position, color, velocity)

        # add itself to the object list
        Collision.add_object(self)
        # dimensions of the rectangle
        self.length = length
        self.height = height

        # create the pygame Rect that will be used to draw the rectangle on the screen
        #self.Rect = pygame.Rect((self.pos.x - length / 2, self.pos.y + height/2), (length, height))


        self.norm = pygame.Vector2(0, 0)
        self.contact_point = pygame.Vector2(0, 0)

        self.interval = [position.x - length / 2, position.x + length / 2]


    def update_p(self, dt, f_total = 0):
        if f_total == 0:
            f_total = self.grav() + self.norm
        self.p += f_total * dt

    def update_v(self):
        self.v = self.p / self.m

    def update_pos(self, dt):
        self.pos += self.v * dt
        #self.Rect.move(self.v.x * dt, self.v.y * dt)

        self.interval[0] = self.pos.x - self.length / 2
        self.interval[1] = self.pos.x + self.length / 2

    def is_box(self)-> bool:
        return True

    def is_sphere(self)->bool:
        return False

    def draw(self, surface: pygame.Surface) -> None:
        rect = pygame.Rect((self.pos.x - self.length / 2, self.pos.y - self.height/2), (self.length, self.height))
        pygame.draw.rect(surface, self.color, rect)



