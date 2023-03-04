import xml.etree.ElementTree as ET
import copy
import os
import json

all_noun_objects = []

def main():
    noun_XML_filenames = os.listdir('../BuNaMo/noun')

    for fname in noun_XML_filenames:
        print('parsing ', fname)
        object_from_one_file = parse_one_xml_file('../BuNaMo/noun/' + fname)
        all_noun_objects.append(object_from_one_file)

    with open('./nouns.json', 'w') as outfile:
        json.dump(all_noun_objects, outfile, ensure_ascii=False)

def parse_one_xml_file(filename):
    mytree = ET.parse(filename)
    root = mytree.getroot()

    json_object = copy.deepcopy(root.attrib)
    for el in root:       
        for item in el.items():
            if item[0] == "default":
                json_object[el.tag] = item[1]
    return json_object

if __name__ == "__main__":
    main()
    # parse_one_xml_file('../BuNaMo/noun/abacas_masc.xml')
