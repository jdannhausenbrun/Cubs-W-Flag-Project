import json

def getGameStatus(response):
    json = response.json()
    print(type(json))
