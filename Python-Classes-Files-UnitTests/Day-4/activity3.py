import json

with open('batman.json', 'r') as json_file:
    data = json.load(json_file)
    for item in data['Search']:
        print(f"Title: {item.get('Title')}\nYear: {item.get('Year')}\nimdbID: {item.get('imdbID')}\nType: {item.get('Type')}\nPoster: {item.get('Poster')}\n")
    print(f"Total Results: {data['totalResults']}\nResponse: {data['Response']}")