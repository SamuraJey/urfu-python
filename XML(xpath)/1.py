from lxml import etree as ET

tree = ET.parse('XML/movies.xml')
root = tree.getroot()

movies_dict = {}

for movie_elem in root.findall('Movie'):
    title_elem = movie_elem.find('Title')
    if not 'runtime' in title_elem.attrib:
        continue
    title = title_elem.text.strip()
    runtime = title_elem.attrib['runtime']

    movies_dict[title] = runtime

print(movies_dict)
