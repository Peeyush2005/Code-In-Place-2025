from karel.stanfordkarel import *

def main():
    while beepers_present():
        if front_is_clear():
            move()
            if front_is_blocked():
                turn_left()
    while no_beepers_present():
        turn_left()
        move()
        if beepers_present():
            turn_right()
            if front_is_clear():
                move()
            else:
                turn_back()
                main()

def turn_right():
    for i in range(3):
        turn_left()
def turn_back():
    for i in range(2):
        turn_left()
# don't change this code
if __name__ == '__main__':
    main()