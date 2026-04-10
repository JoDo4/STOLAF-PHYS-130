import pygame
#from collider import JosiahSparkleCollider

class CBoundary:
    def __init__(self, start_point = pygame.Vector2(0,0), end_point = pygame.Vector2(0,0),
                 color : str = "white", width : int = 1):

        self.start_point = start_point
        self.end_point = end_point

        self.length = pygame.Vector2(end_point - start_point).magnitude()

        self.width = width

        self.color = color

    def draw(self, surface : pygame.Surface):
        pygame.draw.line(surface, self.color, self.start_point, self.end_point, self.width)