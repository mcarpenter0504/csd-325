# Program: Cho-Han Dice Game
# Author: Al Sweigart, adjusted by Madilyn Carpenter
# Date: 2025-06-15
# Assignment: Cho-Han Edits

# Purpose: Play a Japanese dice game where the player bets on whether the total is even (CHO) or odd (HAN). Includes changes for a 12% house fee and bonus payouts for dice totals of 2 or 7.

"""CHANGES MADE:
- Broke original code into functions used within main
- Increase in percentage that goes to the house
- Adjusted messages
- -Bonus added for rolling a total of 2 or 7"""

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

def display_intro():
    # Game introduction and instructions.
    print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. Rolling a total of 2 or 7 will get you a 10 mon bonus B)*
''')

def get_valid_bet(purse):
    # Place your bet.
    print('You have', purse, 'mon. How much do you bet? (or type QUIT)')
    while True:
        pot = input('mjc: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            return int(pot)

def get_valid_bet_choice():
    # Let the player bet cho or han.
    print('    CHO (even) or HAN (odd)?')
    while True:
        bet = input('mjc: ').upper()
        if bet not in ['CHO', 'HAN']:
            print('Please enter either "CHO" or "HAN".')
        else:
            return bet

def roll_dice():
    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def display_dice(dice1, dice2):
    # Reveal the dice results.
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

def evaluate_bet(dice1, dice2, bet):
    # Determine if the player won.
    total = dice1 + dice2
    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet
    return playerWon, total

def apply_bonus(total, purse):
    # Check for bonus on specific totals.
    if total == 2 or total == 7:
        print(f'You rolled a total of {total}! You get a 10 mon bonus!')
        purse += 10
    return purse

def process_result(playerWon, pot, purse):
    # Display the bet results and adjust purse.
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot  # Add the pot to the player's purse.
        house_fee = pot * 12 // 100
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee  # The house fee is 12%.
    else:
        purse -= pot  # Subtract the pot from player's purse.
        print('You lost!')
    return purse

def play_game_loop(purse):
    while True:  # Main game loop.
        pot = get_valid_bet(purse)

        dice1, dice2 = roll_dice()

        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the')
        print('dice and asks for your bet.')
        print()

        bet = get_valid_bet_choice()

        display_dice(dice1, dice2)

        playerWon, total = evaluate_bet(dice1, dice2, bet)

        purse = apply_bonus(total, purse)

        purse = process_result(playerWon, pot, purse)

        # Check if the player has run out of money.
        if purse == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()

def main():
    display_intro()
    purse = 5000
    play_game_loop(purse)

if __name__ == "__main__":
    main()
