import pygame
from .CBoundary import CBoundary
from collision_pygame.collider2 import Collision


class CWall(CBoundary):

    def __init__(self, x= 0, y_range : tuple[int,int] = (0,1), color : str = "white", width : int = 1):

        super().__init__(start_point=pygame.Vector2(x,y_range[0]), end_point=pygame.Vector2(x, y_range[1]),
                         color = color, width = width)

        self.edge = x
        self.y_interval = y_range

        Collision.add_wall(self)