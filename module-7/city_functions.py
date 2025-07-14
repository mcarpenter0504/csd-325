# Program: City-Country Formatter
# Author: Madilyn Carpenter
# Date: 2025-06-22
# Assignment: City Formatter with Input Validation
#
# Purpose: Intake city and country names and format them.

def format_city_country(city, country, language=None, population=None):
    # Return formatted string.
    default = f"{city.title()}, {country.title()}"
    details = []

    if population:
        details.append(f"population {population:,}")
    if language:
        details.append(language.title())

    if details:
        return f"{default} - {', '.join(details)}"
    else:
        return default

def is_valid_name(name):
    # Check if input is valid.
    return name.strip() != "" and not any(char.isdigit() for char in name)

def get_valid_input(prompt):
    # Prompt user until a valid input is recieved.
    while True:
        user_input = input(prompt).strip()
        if is_valid_name(user_input):
            return user_input
        print("Invalid input. Please enter letters only, no numbers or empty spaces.")

def ask_to_continue():
    while True:
        response = input("Would you like to enter another city and country? (yes/no): ").strip().lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def get_optional_population(prompt):
    # Get optional population param
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            return None
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please enter a number or leave blank.")

def get_optional_language(prompt):
    # Get optional language param
    user_input = input(prompt).strip()
    if user_input == "":
        return None
    if any(char.isdigit() for char in user_input):
        print("Invalid input. Please enter letters only or leave blank.")
        return get_optional_language(prompt)
    return user_input

def main():
    while True:
        city = get_valid_input("Enter a city name: ")
        country = get_valid_input(f"Enter the country for {city.title()}: ")
        population = get_optional_population(f"Enter the population for {city.title()} (optional): ")
        language = get_optional_language(f"Enter the primary language for {city.title()} (optional): ")

        print(f"Formatted: {format_city_country(city, country, language, population)}\n")

        if not ask_to_continue():
            break

if __name__ == "__main__":
    main()
