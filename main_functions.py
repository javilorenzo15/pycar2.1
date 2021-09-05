# Import a library of functions called 'pygame'
import pygame
import math

from car_model import Car2
from lane_following import CurvedRoad

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)
BLUE = (0,   0, 255)

size = (1400, 600)
PI = math.pi

def updateSteering(screen, car):
    pygame.draw.arc(screen, GREEN, [20, 20, 250, 200], PI / 4, 3 * PI / 4, 5)
    pygame.draw.arc(screen, RED, [20, 20, 250, 200], 3 * PI / 4, PI, 5)
    pygame.draw.arc(screen, RED, [20, 20, 250, 200], 0, PI / 4, 5)
    pygame.draw.circle(screen, BLACK, [145, 120], 20)
    # rotate tip of needle from 145,10
    # centered at 145,120
    x1 = 145 - 145
    y1 = 10 - 120
    x2 = x1 * math.cos(car.steering_angle) - y1 * math.sin(car.steering_angle)
    y2 = x1 * math.sin(car.steering_angle) + y1 * math.cos(car.steering_angle)
    x = x2 + 145
    y = y2 + 120
    pygame.draw.line(screen, BLACK, [x, y], [145, 120], 5)


def drawRoad(screen):
    # pygame.draw.lines(screen, BLACK, False, [(100,100),(240,100)], 60)

    pygame.draw.lines(screen, GREEN, False, [(100, 385), (250, 385)], 10)
    pygame.draw.arc(screen, GREEN, [100, 90, 300, 300], -PI / 2, 0, 10)
    pygame.draw.arc(screen, GREEN, [100, 90, 300, 300], -PI / 2, 0, 10)

    # pygame.draw.arc(screen,BLACK,[210,90,300,300],-PI/2,0,60)
    # pygame.draw.arc(screen,BLACK,[470,100,300,300],0,PI,60)
    # pygame.draw.arc(screen,BLACK,[710,100,300,300],PI,3*PI/2,60)


def updateSpeedometer(screen, car):
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen

    if car.gear == "D":
        gear_text = font.render("Gear: Drive", True, BLACK)
    elif car.gear == "STOP":
        gear_text = font.render("Gear: Stopped", True, BLACK)
    elif car.gear == "R":
        gear_text = font.render("Gear: Reverse", True, BLACK)
    else:
        gear_text = font.render("Gear: unknown", True, BLACK)

    # Put the image of the gear_text on the screen
    screen.blit(gear_text, [300, 40])

    speed_text = font.render("Speed: " + str(car.speed / 5), True, BLACK)
    screen.blit(speed_text, [300, 60])


def gameLoop(action, car, screen):
    if action == 1 or action == 'a' or action == 'left':
        print('left')
        car.turn(-1)
    elif action == 2 or action == 'd' or action == 'right':
        print('right')
        car.turn(1)


def learningGameLoop():
    print('more code here')


class laneFollowingCar1(Car2):
    def __init__(self):
        super().__init__(RED, 60, 385, screen)
        self.car = super().car
        self.car.constant_speed = True
        self.car.speed = 100
