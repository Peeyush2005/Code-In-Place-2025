from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move_quad()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()
    move_quad()
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_right()
    move_quad()
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()

def left_wall():
    while front_is_clear():

        move()

def move_quad():
    for i in range(4):
        move()


def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()