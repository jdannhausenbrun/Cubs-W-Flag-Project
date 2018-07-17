import requests

from constants import API_KEY

URL = "http://api.sportradar.us/mlb/trial/v6.5/en/games/d4f1ecee-8318-42e7-8ce9-90411d089dfa/summary.json?api_key=%s" %(API_KEY)

r = requests.get(url = URL)
if r.status_code != 200:
    print("Error Reading Data")
else:
    print(r.json())
