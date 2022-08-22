
# Importing pygame module
from functools import reduce
from turtle import update
import pygame
from pygame.locals import *
import random

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((600, 600))

running = [True]

difficulty = ["easy", "medium", "hard", "expert"]

move_ball_event = pygame.USEREVENT + 0
update_ball_color_event = pygame.USEREVENT + 1


ball_color_red = (255, 50, 50)
ball_color_black = (0, 0, 0)
ball_position = [100, 100]
ball_size = [30]
points = [0]
health = [100]


def move_ball():
    position_x = random.randint(40, 560)
    position_y = random.randint(40, 560)
    ball_position[0] = position_x
    ball_position[1] = position_y


def get_ball_position():
    return ball_position


def change_ball_size():
    new_ball_size = random.randint(5, 40)
    ball_size[0] = new_ball_size


def get_mouse_click_position():
    cursor_position = pygame.mouse.get_pos()
    return cursor_position


def get_ball_radius():
    return ball_size[0]


def verify_circle_hit():
    # get location of circle
    ball_position = get_ball_position()
    # get location of cursor
    mouse_click_position = get_mouse_click_position()
    # get ball radius
    ball_radius = get_ball_radius()
    # see if they the cursor is within the radius of the circle
    is_within_radius = radius_check(
        ball_position, mouse_click_position, ball_radius)

    if is_within_radius:
        add_points()
        return True

    # if its true, add point
    else:
        reduce_health()
        if (health[0] <= 0):
            print("You lose!")
            running[0] = False
        return False
    # if not, reduce health


def radius_check(ball_position, mouse_click_position, ball_radius):
    if abs(mouse_click_position[0] - ball_position[0]) <= ball_radius:
        print(abs(mouse_click_position[0] - ball_position[0]))
        if abs(mouse_click_position[1] - ball_position[1]) <= ball_radius:
            print(abs(mouse_click_position[1] -
                  ball_position[1]) <= ball_radius)
            return True
    else:
        return False


def add_points():
    points[0] += 1
    print("Points scored: ", points)


def reduce_health():
    health[0] -= 10
    print("Health: ", health)


def update_ball_color():
    print("here")
    window.fill((255, 255, 255))
    pygame.display.update()


def render():
    window.fill((255, 255, 255))
    pygame.draw.circle(window, ball_color_red, ball_position, ball_size[0], 0)
    pygame.display.update()


allow_hit = [True]


def target_hit_animation():
    allow_hit[0] = False
    pygame.draw.circle(window, ball_color_black,
                       ball_position, ball_size[0], 0)
    pygame.display.update()
    pygame.time.wait(200)
    window.fill((255, 255, 255))
    pygame.display.update()


render()


pygame.time.set_timer(move_ball_event, 700)

while running[0]:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if (allow_hit[0]):
                if verify_circle_hit():
                    target_hit_animation()
        elif event.type == move_ball_event:
            allow_hit[0] = True
            move_ball()
            change_ball_size()
            render()

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
