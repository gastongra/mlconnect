#!/usr/bin/env python
import requests
from json import loads
import logging


class MLConnect:
    def __init__(self, site):
        self.site = site  # i.e. "MLA"
        self.baseSearchURL = "https://api.mercadolibre.com/sites/" + self.site + "/search"
        self.baseItemURL = "https://api.mercadolibre.com/items/"

    def getCategoryItems(self, category, offset):
        url = self.baseSearchURL
        params = dict(
            category=category,
            limit=100,
            offset=str(offset)
        )
        response = requests.get(url=url, params=params)
        return loads(response.text)

    def getItem(self, item):
        url = self.baseItemURL + item
        response = requests.get(url=url)
        return loads(response.text)


# Main
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Ejemplo de como recuperar un item con la API de ML.")
    logger.info("Ahí vamos ...")
    ml = MLConnect('MLA')
    item = ml.getItem('MLA616294537')
    item_id = item['id']
    site_id = item["site_id"]
    title = item['title']
    seller_id = item['seller_id']
    price = item['price']
    available_quantity = item['available_quantity']
    sold_quantity = item['sold_quantity']
    listing_type_id = item['listing_type_id']
    condition = item['condition']
    logger.info("'" + item['id'] + "','" + item['site_id'] + "','" +
                item['title'] + "','" + str(item['seller_id']) +
                "'," + str(item['price']) + "," +
                str(item['available_quantity']) + "," +
                str(item['sold_quantity']) + ",'" +
                str(item['listing_type_id']) + "','" +
                str(item['condition']) + "'")
