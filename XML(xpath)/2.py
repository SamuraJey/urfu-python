import json, xmltodict

with open("XML/movies.xml", errors='ignore') as f:
    o = xmltodict.parse(f.read())


print(json.dumps(o))
    

