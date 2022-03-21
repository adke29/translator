import json


f = open('c2e.json',"r",encoding="utf-8")
data = json.load(f)
print(data)

f.close()