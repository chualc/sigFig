# https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
tree = ET.parse('xlmFile.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)

    #country {'name': 'Liechtenstein'}
    #country {'name': 'Singapore'}
    #country {'name': 'Panama'}

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

