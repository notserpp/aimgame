
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
allow_hit = [True]
is_hit = [False]
game_speed = [2000]

move_ball_event = pygame.USEREVENT + 0
pygame.time.set_timer(move_ball_event, game_speed[0])


ball_color_red = (255, 50, 50)
ball_color_black = (0, 0, 0)
ball_position = [100, 100]
ball_size = [30]
points = [0]
health = [100]


def move_ball():
    position_x, position_y = random.randint(40, 560), random.randint(40, 560)
    ball_position[0], ball_position[1] = position_x, position_y


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
        reduce_health(10)
        if (health[0] <= 0):
            print("You lose!")
            running[0] = False
        return False
    # if not, reduce health


def radius_check(ball_position, mouse_click_position, ball_radius):
    if abs(mouse_click_position[0] - ball_position[0]) <= ball_radius:
        if abs(mouse_click_position[1] - ball_position[1]) <= ball_radius:
            return True
    else:
        return False


def add_points():
    points[0] += 1
    print("Points scored: ", points)


def reduce_health(points):
    health[0] -= points
    print("Health: ", health)


def update_ball_color():
    window.fill((255, 255, 255))
    pygame.display.update()


def target_hit_animation():
    allow_hit[0] = False
    is_hit[0] = True
    pygame.draw.circle(window, ball_color_black,
                       ball_position, ball_size[0], 0)
    pygame.display.update()
    pygame.time.wait(200)
    window.fill((255, 255, 255))
    pygame.display.update()


def did_hit():
    if is_hit[0] == False:
        reduce_health(1)


def render():
    window.fill((255, 255, 255))
    pygame.draw.circle(window, ball_color_red, ball_position, ball_size[0], 0)
    pygame.display.update()


def update_game_speed():
    game_speed[0] -= 100
    print((game_speed[0]))
    pygame.time.set_timer(move_ball_event, game_speed[0])


def allow_new_hit():
    allow_hit[0] = True


def is_not_hit():
    is_hit[0] = False


render()


while running[0]:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if (allow_hit[0]):
                if verify_circle_hit():
                    target_hit_animation()
                    update_game_speed()
        elif event.type == move_ball_event:
            move_ball()
            change_ball_size()
            did_hit()
            render()
            allow_new_hit()
            is_not_hit()

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False
