# Program: On the Wall
# Author: Madilyn Carpenter
# Date: 2025-06-08
# Assignment: Bottles of Beer Song

# Purpose: Print beer song starting with number entered from user prompt

def get_valid_bottle_count():
    # Prompts the user until a valid whole number > 0 is entered.
    while True:
        user_input = input("Enter number of bottles: ").strip()

        if not user_input.isdigit():
            print("Invalid input. Please enter a whole number greater than 0.")
            continue

        bottle_count = int(user_input)
        if bottle_count < 1:
            print("Please enter a number greater than 0.")
        else:
            return bottle_count


def sing_bottles_song(starting_bottles):
    # Prints the countdown song from starting_bottles to 0.
    for count in range(starting_bottles, 0, -1):
        if count > 1:
            next_count = count - 1
            bottle_word = "bottle" if next_count == 1 else "bottles"
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            print(f"Take one down and pass it around, {next_count} {bottle_word} of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, 0 bottles of beer on the wall.\n")

def main():
    bottle_count = get_valid_bottle_count()
    sing_bottles_song(bottle_count)


if __name__ == "__main__":
    main()
