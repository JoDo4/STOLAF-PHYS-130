from .CBoundary import CBoundary
from vpython import *
from collider import JosiahSparkleCollider

class CFloor(CBoundary):
    def __init__(self, height=1, depth=1, x_range : tuple[int, int]= (0,1), y = 0, z_range : tuple[int,int] = (0,0), color = color.white):
        super().__init__(height=height, depth = depth, start_point=vector(x_range[0],y,z_range[0]), end_point=vector(x_range[1], y, z_range[1]), color = color)

        JosiahSparkleCollider.add_floor(self)

        self.x_interval = x_range
        self.top = y
        self.z_interval = z_range