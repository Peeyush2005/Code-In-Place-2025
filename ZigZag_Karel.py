from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    # Continuously perform actions while the front is clear
    while front_is_clear():
        if front_is_blocked():
            # If front is blocked (shouldn’t happen inside while loop logically, but included)
            moving1()
        else:
            # Otherwise, perform beeper-filling routine
            moving()

def front_block():
    # Check if Karel can turn right to move to the next row
    if right_is_clear():
        turn_right()   # Turn right
        move()         # Move to next row
        turn_right()   # Turn right again to start moving in the opposite direction
    else:
        # If right is blocked (no more rows), return to start
        moving_back()

def moving():
    # Move across the row placing beepers in every cell
    while front_is_clear():
        put_beeper()   # Place a beeper in current cell
        move()         # Move forward
    put_beeper()       # Place a beeper in the last cell
    moving_back()      # Return to the start of the row
    front_block()      # Move to the next row if possible

def moving1():
    # Move forward continuously without placing beepers
    while front_is_clear():  
        move()

def moving_back():
    # Move back to the start of the row
    turn_back()       # Turn around
    while front_is_clear():
        move()        # Move backward to starting point

def turn_back():
    # Turn around 180 degrees
    for i in range(2):
        turn_left()

def turn_right():
    # Turn right (90 degrees)
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
