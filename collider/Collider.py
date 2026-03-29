from vpython import vector

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
                    # CURRENTLY NOT ACTUAL PHYSICAL COLLISION
                    temp1 = object1.v
                    temp2 = object2.v

                    # update velocity and momentum of object1
                    object1.v = ((object1.m - object2.m)/(object1.m + object2.m) * temp1 +
                             (2*object2.m)/(object1.m + object2.m) * temp2)
                    object1.p = object1.v * object1.m

                    # update velocity and momentum of object2
                    object2.v = ((2*object1.m)/(object1.m + object2.m)*temp1 +
                             (object2.m - object1.m)/(object1.m + object2.m) * temp2)
                    object2.p = object2.v * object2.m


    def handle_floor_collision(self) -> None:
        # check if each object is colliding with each floor
        for floor in self.floors:
            for ob in self.object_list:
                if ob.is_sphere():
                    # object is sphere
                    if ob.pos.y - ob.radius <= floor.top:
                        ob.pos.y = floor.top + ob.radius
                        ob.shape.y = ob.pos.y

                        ob.norm = -ob.grav()
                        ob.contact_point = ob.pos - vector(0, ob.radius, 0)

                        ob.v.y = 0
                        ob.p.y = 0
                    else:
                        ob.norm = vector(0, 0, 0)
                        ob.contact_point = None
                else:
                    # object is box
                    if ob.pos.y - ob.height / 2 <= floor.top:
                        ob.pos.y = floor.top + ob.height / 2
                        ob.shape.y = ob.pos.y

                        ob.norm = -ob.grav()
                        ob.contact_point = ob.pos - vector(0, ob.length / 2, 0)

                        ob.v.y = 0
                        ob.p.y = 0
                    # if box is not on ground
                    else:
                        ob.norm = vector(0, 0, 0)
                        ob.contact_point = None


    def handle_wall_collision(self)-> None:
        # check if each object is colliding with each wall
        for wall in self.walls:
            for ob in self.object_list:
                if ob.interval[0] < wall.edge < ob.interval[1]:
                    # snap the edge of the object to the edge of the wall
                    if ob.v.x > 0:
                        # update center of object
                        ob.pos.x = wall.edge - (ob.interval[1] - ob.pos.x)
                        ob.shape.x = ob.pos.x
                        # update interval
                        ob.interval[1] = wall.edge
                        ob.interval[0] = ob.pos.x - (ob.interval[1] - ob.pos.x)

                        ob.v.x = -ob.v.x
                        ob.p.x = ob.v.x * ob.m
                    elif ob.v.x < 0:
                        # update center of object
                        ob.pos.x = wall.edge - (ob.interval[0] - ob.pos.x)
                        ob.shape.x = ob.pos.x

                        ob.interval[0] = wall.edge
                        ob.interval[1] = ob.pos.x + (ob.pos.x - ob.interval[0])

                        ob.v.x = -ob.v.x
                        ob.p.x = ob.v.x * ob.m






    def update(self, dt):
        # check if an object is colliding with another object or boundary
        self.handle_1D_collision()
        self.handle_floor_collision()
        self.handle_wall_collision()


        # update each objects momentum, velocity, and position
        for ob in self.object_list:
            ob.update_p(dt)
            ob.update_v()
            ob.update_pos(dt)



JosiahSparkleCollider : Collider = Collider()

