import xml.etree.ElementTree as ET

tree_client = ET.parse('clientFile.xml');
root_client = tree_client.getroot()
tree_our = ET.parse('ourFile.xml');
root_our = tree_our.getroot()


for product in root_client.iter('product'):
    print(product.attrib)
for offer in root_our.iter('offer'):
    print(offer.attrib)
    l = list(offer.attrib)
    print(l[0])
#for price in root_our.iter('price'):
 #   print(price.attrib)
