import requests
import json

url = 'https://www.whichbook.net/api/v1/search?q4=8&q9=2&q2=3&q8=3&q10=3&q12=3&q1=4&pagesize=500'
response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully:")
    data = response.json()
else:
    print(f"Failed. Status code: {response.status_code}")

with open('dataset4.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

