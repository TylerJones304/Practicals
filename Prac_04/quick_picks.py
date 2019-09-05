import random

MAX_NUMBER = 45
MIN_NUMBER = 1
NUMBERS_IN_LINE = 6


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks <= 0:
        print("Invalid number. Must be at least 1")
        number_of_quick_picks = input("How many quick picks? ")

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_IN_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_picks:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(quick_picks)


main()

# numbers = []
# for i in range(5):
#     number = int(input("Enter number: "))
#     numbers.append(number)
