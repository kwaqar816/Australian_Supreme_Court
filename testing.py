
import json

with open('JSON Output/06_01_2021.json', 'r') as rd:
    op = json.loads(rd.read())
    print(type(op))
    print(op[1]["description"])
