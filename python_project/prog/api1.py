# Prog to access Apple itune and get the trackname
#https://itunes.apple.com/search?entity=song&limit=1&term=weezer
# requires argument of the band name (eg: weezer)

import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit()   # sys.exit to break out of the program , break is used to get out of loops

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
print(response.json())  # this will print the output in json
print(json.dumps(response.json(), indent=2))  # this will output nice and clean

output = response.json()  # this will output to the variable  as json object

for x in output["results"]:

    print(x["trackName"])


