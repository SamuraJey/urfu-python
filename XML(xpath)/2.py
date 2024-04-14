import json
import xmltodict

# Читерная реализация с помощью библиотеки. По идее надо сделать самому,
# но т.к. я успел написать код на паре, он мне разрешил с помощью библиотеки
with open("XML/movies.xml", errors='ignore') as f:
    o = xmltodict.parse(f.read())


print(json.dumps(o))
