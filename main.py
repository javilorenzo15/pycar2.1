# Import a library of functions called 'pygame'
import pygame
import math

from car_model import Car2
from lane_following import CurvedRoad
from main_functions import *
# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)

size = (1400, 600)
PI = math.pi

if __name__ == "__main__":

    t = 0

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("mdeyo car sim")
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    car = Car2(RED, 60, 385, screen)
    road = CurvedRoad(1200, 60, 385, '45')
    car.constant_speed = True
    car.speed = 100
    # car = laneFollowingCar1()

    screen.fill(WHITE)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_UP]:
            car.accelerate(1)
        if keys[pygame.K_DOWN]:
            car.accelerate(-1)
        if keys[pygame.K_LEFT]:
            car.turn(-1)
        if keys[pygame.K_RIGHT]:
            car.turn(1)
        # print(t)
        # inputKey = input('press a key')
        # gameLoop(inputKey,car,screen)
        t += 1
        # t = 114 if driving straight to x=1200 at car.speed=100
        # t =
        for event in pygame.event.get():  # User did something

            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            elif event.type == pygame.KEYDOWN:
                # print("User pressed a key.")
                if event.key == pygame.K_LEFT:
                    car.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    car.turn(1)
                elif event.key == pygame.K_UP:
                    car.accelerate(1)
                elif event.key == pygame.K_DOWN:
                    car.accelerate(-1)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    car.release_down(-1)
                if event.key == pygame.K_UP:
                    car.release_down(1)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("User pressed a mouse button")

        # --- Game logic should go here

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # --- Game logic and drawing code combined

        drawRoad(screen)
        road.plotRoad(screen)

        rate = 10
        car.update(1 / rate)
        updateSteering(screen, car)
        updateSpeedometer(screen, car)
        print(road.reward(car))

        if(t > 2000):
            car.speed = 0
            print('done!')
            done = True

        if(car.pose[0] > 1200):
            print('reached x=1200')
            car.speed = 0
            done = True

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(rate)
