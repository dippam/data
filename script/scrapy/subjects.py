import json
from pprint import pprint

with open('test.json') as file:
    documents = json.load(file)

pprint(documents)
