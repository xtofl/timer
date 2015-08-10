#!/usr/bin/env python

from time import sleep

def timer(total_ticks):
    ticks_left = total_ticks
    while ticks_left != 0:
        print("{}/{}".format(ticks_left, total_ticks))
        sleep(1)
        ticks_left = ticks_left - 1

def buzz():
    print("TODO: ... buzzzzz")

from pygame.locals import *
import pygame

def game():
    screen = pygame.display.set_mode((1024, 768), DOUBLEBUF)
    car = pygame.image.load('car.png')
    screen.blit(car, (50, 100))
    pygame.display.flip()
    timer(15)

game()

