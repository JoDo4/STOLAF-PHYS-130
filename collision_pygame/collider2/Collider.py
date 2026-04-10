import pygame
from pygame import Vector2 as Vector

class Collider:
    def __init__(self):
        self.object_list = []
        self.floors = []
        self.walls = []


    def add_object(self, obj) -> None:
        self.object_list.append(obj)

    def add_floor(self, floor) -> None:
        self.floors.append(floor)


    def add_wall(self, wall) -> None:
        self.walls.append(wall)

    def handle_1D_collision(self) -> None:

        # sort the list from the lowest starting value to the highest starting value
        self.object_list = sorted(self.object_list, key=lambda object: object.interval[0])

        # look for collisions

        for i in range(len(self.object_list)):
            object1 = self.object_list[i]

            for j in range(i+1, len(self.object_list)):
                object2 = self.object_list[j]

                # check if the left side of sphere2 is to the right of sphere1
                # AKA not overlapping
                if object2.interval[0] > object1.interval[1]:
                    break
                # update velocity and momentum
                else:
                    temp1 = object1.v.x
                    temp2 = object2.v.x

                    # update velocity and momentum of object1
                    object1.v.x = ((object1.m - object2.m)/(object1.m + object2.m) * temp1 +
                             (2*object2.m)/(object1.m + object2.m) * temp2)
                    object1.p.x = object1.v.x * object1.m

                    # update velocity and momentum of object2
                    object2.v.x = ((2*object1.m)/(object1.m + object2.m)*temp1 +
                             (object2.m - object1.m)/(object1.m + object2.m) * temp2)
                    object2.p.x = object2.v.x * object2.m

                    # update position of the two objects
                    overlap = object1.interval[1] - object2.interval[0]

                    object1.pos.x = object1.pos.x - overlap/2
                    object2.pos.x = object2.pos.x + overlap/2
    """
    def handle_2D_collision(self) -> None:

        # sort the list from the lowest starting value to the highest starting value
        self.object_list = sorted(self.object_list, key=lambda object: object.interval[0])

        # look for collisions
        for i in range(len(self.object_list)):
            object1 = self.object_list[i]

            for j in range(i + 1, len(self.object_list)):
                object2 = self.object_list[j]

                # check if the left side of sphere2 is to the right of sphere1
                # AKA not overlapping
                if object2.interval[0] > object1.interval[1]:
                    break
                # update velocity and momentum
                else:

                    if object1.is_sphere():
                        temp_vec = object2.pos - object1.pos
                        if temp_vec.mag() <= object1.radius:
                            # update velocity and magnitude
                            temp1 = object1.v
                            temp2 = object2.v
                            
                            # update object 1
                            object1.v = temp1 - (2 * object2.m)/(object1.m + object2.m) * (

                    
                    
                    
                    
                    temp1 = object1.v.x
                    temp2 = object2.v.x

                    # update velocity and momentum of object1
                    object1.v.x = ((object1.m - object2.m) / (object1.m + object2.m) * temp1 +
                                   (2 * object2.m) / (object1.m + object2.m) * temp2)
                    object1.p.x = object1.v.x * object1.m

                    # update velocity and momentum of object2
                    object2.v.x = ((2 * object1.m) / (object1.m + object2.m) * temp1 +
                                   (object2.m - object1.m) / (object1.m + object2.m) * temp2)
                    object2.p.x = object2.v.x * object2.m

                    # update position of the two objects
                    overlap = object1.interval[1] - object2.interval[0]

                    object1.pos.x = object1.pos.x - overlap / 2
                    object2.pos.x = object2.pos.x + overlap / 2
                    
"""
    def handle_floor_collision(self) -> None:
        # check if each object is colliding with each floor
        for floor in self.floors:
            for ob in self.object_list:
                if ob.is_sphere():
                    # object is sphere
                    if ob.pos.y + ob.radius + floor.width/2 >= floor.top:
                        # set the bottom of the sphere to edge of floor
                        ob.pos.y = floor.top - ob.radius - floor.width/2 + 1


                        ob.norm = -ob.grav()
                        ob.contact_point = ob.pos - Vector(0, ob.radius + floor.width/2+1)

                        ob.v.y = 0
                        ob.p.y = 0
                    else:
                        ob.norm = Vector(0, 0)
                        ob.contact_point = None
                else:
                    # object is box
                    if ob.pos.y + ob.height/2 + floor.width/2 >= floor.top:
                        ob.pos.y = floor.top - ob.height / 2 - floor.width/2 + 1


                        ob.norm = -ob.grav()
                        ob.contact_point = ob.pos - Vector(0, ob.length/2 + floor.width/2+1)

                        ob.v.y = 0
                        ob.p.y = 0
                    # if box is not on ground
                    else:
                        ob.norm = Vector(0, 0)
                        ob.contact_point = None


    def handle_wall_collision(self)-> None:
        # check if each object is colliding with each wall
        for wall in self.walls:
            for ob in self.object_list:
                if ob.interval[0] < wall.edge + wall.width/2 < ob.interval[1] or ob.interval[0] < wall.edge - wall.width/2 < ob.interval[1]:
                    # snap the edge of the object to the edge of the wall
                    half_width = ob.interval[1] - ob.pos.x
                    if ob.v.x > 0:

                        # update center of object
                        ob.pos.x = wall.edge - half_width - wall.width/2 - 1

                        # update interval
                        ob.interval[1] = ob.pos.x + half_width
                        ob.interval[0] = ob.pos.x - half_width

                        ob.v.x = -ob.v.x
                        ob.p.x = ob.v.x * ob.m
                    elif ob.v.x < 0:
                        # update center of object
                        ob.pos.x = wall.edge + half_width + wall.width/2 + 1


                        ob.interval[0] = ob.pos.x - half_width
                        ob.interval[1] = ob.pos.x + half_width

                        ob.v.x = -ob.v.x
                        ob.p.x = ob.v.x * ob.m






    def update(self, dt : float, surface) -> None:
        # check if an object is colliding with another object or boundary
        self.handle_1D_collision()
        self.handle_floor_collision()
        self.handle_wall_collision()

        # draw each wall
        for wall in self.walls:
            wall.draw(surface)

        # draw each floor
        for floor in self.floors:
            floor.draw(surface)



        # update each objects momentum, velocity, and position. Then draw each object
        for ob in self.object_list:
            ob.update_p(dt)
            ob.update_v()
            ob.update_pos(dt)
            ob.draw(surface)

    def clear_collider(self) -> None:
        self.walls = []
        self.floors = []
        self.object_list = []


Collision = Collider()

