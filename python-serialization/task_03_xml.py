
#!/usr/bin/env python3
"""Serialize and deserialize Python dictionaries using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    for element in root:
        dictionary[element.tag] = element.text

    return dictionary
