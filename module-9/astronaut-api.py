import requests
import json

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def main():
    url = 'http://api.open-notify.org/astros.json'
    data = get_api_data(url)
    if data:
        jprint(data)
    else:
        print("No data returned.")

if __name__ == "__main__":
    main()
