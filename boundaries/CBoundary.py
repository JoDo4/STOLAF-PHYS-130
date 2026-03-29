from vpython import *
#from collider import JosiahSparkleCollider

class CBoundary:
    def __init__(self, start_point = vector(0,0,0), end_point = vector(0,0,0), color = color.white, depth = 1, height = 1):
        self.start_point = start_point
        self.end_point = end_point

        self.length = mag(end_point - start_point)
        self.axis = vector(end_point - start_point)/self.length

        self.center = vector((start_point.x + end_point.x) / 2 + height * self.axis.y/2, (start_point.y + end_point.y)/2 - height*self.axis.x/2, 0)

        self.height = height
        self.depth = depth

        self.color = color

        self.shape = box(pos = self.center,length = self.length,height = self.height,depth = self.depth, axis = self.axis, color = self.color)