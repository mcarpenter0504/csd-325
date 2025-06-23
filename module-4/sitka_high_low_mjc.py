# Program: Sitka Weather Viewer
# Author: Madilyn Carpenter
# Date: 2025-06-22
# Assignment: Weather Viewer Edits

# Purpose: Display graphs of daily high or low temperatures from Sitka.

"""CHANGES MADE:
- Broke code into functions
- Added a menu allowing users to choose temp type or exit
- Loaded both high and low temperatures from the CSV file
- Added looping
- Plotted low temperatures in blue and high temperatures in red
- Added input validation
- Added message upon exit
- Used sys.exit() to end program"""

import csv
import sys
from datetime import datetime
import matplotlib.pyplot as plt

def load_data(file_name):
    # Loads weather data from the CSV file.
    
    dates, highs, lows = [], [], []
    with open(file_name) as f:
        reader = csv.reader(f)
        next(reader)  # skip header row

        for row in reader:
            try:
                date = datetime.strptime(row[2], '%Y-%m-%d')
                high = int(row[5])
                low = int(row[6])
            except ValueError:
                continue  # skip bad rows
            dates.append(date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

def plot_data(dates, temps, title, color):
    # Plots temperature data.
    
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)
    ax.set_title(title, fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

def show_menu():
    # Displays the main menu and returns the user's choice.
    
    print("\nMenu:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    return input("Enter your choice (1/2/3): ").strip()

def menu_loop(file_name):
    # Handles the main program loop.
    
    dates, highs, lows = load_data(file_name)

    while True:
        choice = show_menu()

        if choice == '1':
            plot_data(dates, highs, "Daily High Temperatures - 2018", 'red')
        elif choice == '2':
            plot_data(dates, lows, "Daily Low Temperatures - 2018", 'blue')
        elif choice == '3':
            print("\nThank you for using the Weather Viewer.")
            sys.exit(0)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def main():
    file_name = 'sitka_weather_2018_simple.csv'
    menu_loop(file_name)

if __name__ == "__main__":
    main()
