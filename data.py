import requests
import json

url = 'https://www.whichbook.net/api/v1/search/searchcharplot?race=0&age=0&sexuality=0&gender=0&plot=0&pageNumber=1'
response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully:")
    data = response.json()
else:
    print(f"Failed. Status code: {response.status_code}")

with open('datset1.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

