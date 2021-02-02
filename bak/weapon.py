#!/usr/bin/python3
import xml.etree.ElementTree as ET
tree = ET.parse('/home/pluto/tmp/dest/weapon.xml')
root = tree.getroot()
for child in root:
    print(child.tag,child.attrib)
#print(root)
