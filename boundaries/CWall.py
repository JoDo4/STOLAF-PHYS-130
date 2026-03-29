from .CBoundary import CBoundary
from vpython import *
from collider import JosiahSparkleCollider


class CWall(CBoundary):

    def __init__(self, height=1, depth=1, x= 0, y_range : tuple[int,int] = (0,1), z_range : tuple[int,int] = (0,0), color = color.white):
        super().__init__(height=height, depth = depth, start_point=vector(x,y_range[0],z_range[0]), end_point=vector(x, y_range[1], z_range[1]), color = color)

        JosiahSparkleCollider.add_wall(self)

        self.edge = x
        self.y_interval = y_range
        self.z_interval = z_range
