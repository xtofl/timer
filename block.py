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

timer(15)
buzz()

