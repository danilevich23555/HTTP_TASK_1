import requests
from pprint import pprint

class hero:
    def __init__(self, name):
        self.name = name
        url = "https://superheroapi.com/api/2619421814940190/search/"+name
        resp = requests.get(url=url)
        self.intelligence = (int((resp.json()['results'])[0]['powerstats']['intelligence']))
    def intelligence_levl (self):
        return self.intelligence

characters = ['Hulk', 'Thanos', 'Captain America']

def smart_character(characters):
    max_intelligence = 0
    for character in characters:
        if hero(character).intelligence_levl() > max_intelligence:
            max_intelligence = hero(character).intelligence_levl()
            smart = character
    return print(f'Самый умный супергерой {smart}, его интелект состовляет {max_intelligence}.')


smart_character(characters)



