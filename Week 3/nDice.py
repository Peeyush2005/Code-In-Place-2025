import random

def main():
    side=int(input("How many sides does your dice have? "))
    roll=random.randint(1,side)
    print("Your roll is ",roll)

if __name__ == '__main__':
    main()