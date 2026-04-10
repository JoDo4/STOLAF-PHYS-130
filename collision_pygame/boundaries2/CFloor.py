import pygame
from .CBoundary import CBoundary
from collision_pygame.collider2 import Collision

class CFloor(CBoundary):
    def __init__(self, x_range : tuple[int, int]= (0,1), y : int = 0, color : str = "white", width : int = 1):

        super().__init__( start_point=pygame.Vector2(x_range[0],y), end_point=pygame.Vector2(x_range[1], y),
                          color = color, width = width)

        self.x_interval = x_range
        self.top = y

        Collision.add_floor(self)