import requests
import json

url = 'https://www.whichbook.net/api/v1/search?pagesize=499&page=1'
response = requests.get(url)

if response.status_code == 200:
    print("Data fetched successfully:")
    data = response.json()


    filtered_data = []
    for item in data['books']:
        filtered_item = {   
            "id": item.get("id"),
            "title": item.get("title"),
            "author": item.get("author"),
            "review": item.get("review"),
            "publicationYear": item.get("publicationYear"),
            "imageUrl": item.get("imageUrl"),
        }
        filtered_data.append(filtered_item)
    
    with open('data.json', 'w') as json_file:
        json.dump(filtered_data, json_file, indent=4)

else:
    print(f"Failed. Status code: {response.status_code}")


