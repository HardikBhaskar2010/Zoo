import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the ROLL-A-DICE simulator!")
    response = 'y'
    
    while response == 'y':
        result = roll_dice()
        
        if result == 1:
            print("---------")
            print("|       |")
            print("|   *   |")
            print("|       |")
            print("---------")
        elif result == 2:
            print("---------")
            print("| *     |")
            print("|       |")
            print("|     * |")
            print("---------")
        elif result == 3:
            print("---------")
            print("| *     |")
            print("|   *   |")
            print("|     * |")
            print("---------")
        elif result == 4:
            print("---------")
            print("| *   * |")
            print("|       |")
            print("| *   * |")
            print("---------")
        elif result == 5:
            print("---------")
            print("| *   * |")
            print("|   *   |")
            print("| *   * |")
            print("---------")
        elif result == 6:
            print("---------")
            print("| * * * |")
            print("|       |")
            print("| * * * |")
            print("---------")

        response = input("Do you want to roll again? (y/n): ").lower()

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
