import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

print(root.tag)

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])

for movie in root.iter('movie'):
    print(movie.attrib)

for movie in root.findall("./movie/[stars='10']"):
    print(movie.attrib)

for movie in root.findall('movie'):
    for child in movie.getiterator():
        print(child)
