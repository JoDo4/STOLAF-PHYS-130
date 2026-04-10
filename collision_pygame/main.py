import pygame
from .objects2 import *
from .boundaries2 import *
from collision_pygame.collider2 import Collision

pygame.init()

def example():
    # Set the width and height of the screen (width, height), and name the window.
    Collision.clear_collider()

    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Collision")

    tick = 100
    dt = 1.0/tick

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    CFloor((0,700), 550, "white", 10)
    CWall(100, (695, 100), "white", 5)
    CWall(600, (695, 100), "white", 5)

    CSphere(20, 20, pygame.Vector2(350, 200), "red", pygame.Vector2(200,100))
    CSphere(10, 9, pygame.Vector2(150, 200), "red", pygame.Vector2(-100, 0))
    CSphere(15, 10, pygame.Vector2(400, 500), "orange", pygame.Vector2(200,100))
    #CSphere(10, 2, pygame.Vector2(200, 200), "red", pygame.Vector2(0, 0))
    CBox(20, 30, 10, pygame.Vector2(200,200), "blue", pygame.Vector2(0,0))
    CBox(20,20, 10, pygame.Vector2(220,300), "green", pygame.Vector2(0,0))

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True  # Flag that we are done so we exit this loop.

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        Collision.update(dt= dt, surface=screen)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(tick)  # limits FPS to 60

    pygame.quit()
