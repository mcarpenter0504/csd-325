import requests
import json

def get_api_data(url):
    response = requests.get(url)
    return response

def print_raw(response):
    print(response.text)

def print_formatted(response):
    obj = response.json()
    print(json.dumps(obj, sort_keys=True, indent=4))

def get_user_choice(response):
    print("Choose response type:")
    print("1 - Raw")
    print("2 - Formatted")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        print_raw(response)
    elif choice == '2':
        print_formatted(response)
    else:
        print("Invalid choice. Please enter 1 or 2.")

def main():
    url = 'https://newton.now.sh/api/v2/factor/x^2-1'
    response = get_api_data(url)

    if not response.ok:
        print(f"Error: status code - {response.status_code}")
        return

    get_user_choice(response)

if __name__ == "__main__":
    main()
