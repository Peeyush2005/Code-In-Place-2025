# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    age = int(input("Enter an age in calendar years: "))
    dog_age = DOG_YEARS_MULTIPLIER * age
    print(f"That's {dog_age} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()