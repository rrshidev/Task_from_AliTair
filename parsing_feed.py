# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

partner_tree = ET.parse('clientFile.xml');
partner_root = partner_tree.getroot()
my_tree = ET.parse('ourFile.xml');
my_root = my_tree.getroot()


def partner_feed_parsing():
    products = {}
    for product in partner_root.iter('product'):
        product_id = product.attrib.get('prodID')
        summ = 0
        for assort in product.iter('assort'):
            quantity = assort.attrib.get('sklad')
            summ += int(quantity)
        for price in product.iter('price'):
            BaseRetailPrice = price.attrib.get('BaseRetailPrice')
            BaseWholePrice = price.attrib.get('BaseWholePrice')
            RetailPrice = price.attrib.get('RetailPrice')
            WholePrice = price.attrib.get('WholePrice')
        product_dict = {
            'id': product_id,
            'BaseRetailPrice': BaseRetailPrice,
            'BaseWholePrice': BaseWholePrice,
            'RetailPrice': RetailPrice,
            'WholePrice': WholePrice,
            'quantity': summ,
        }
        products[product_id] = product_dict
    return products


def main():
    products = partner_feed_parsing()

    for offer in my_root.iter('offer'):
        offer_id = offer.attrib.get('id')
        price_tag = offer.find('price')
        try:
            partner_product = products[offer_id]
        except KeyError:
            print('Offer with id = {} not found in partner file'.format(offer_id))
            continue

        price_tag.set('BaseRetailPrice', partner_product['BaseRetailPrice'])
        price_tag.set('BaseWholePrice', partner_product['BaseWholePrice'])
        price_tag.set('RetailPrice', partner_product['RetailPrice'])
        price_tag.set('WholePrice', partner_product['WholePrice'])
        quantity_tag = offer.find('quantity')
        quantity_tag.text = str(partner_product['quantity'])

    my_tree.write('ourFile.xml', encoding="utf-8")
    return print('Done!')


main()
