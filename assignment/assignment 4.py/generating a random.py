import random
def generate_random_number(first, last):
    return random.randint(first,last)
def main():
    print("Random number between 1 and 100:", generate_random_number(1, 100))
if __name__ == "__main__":
    main()
