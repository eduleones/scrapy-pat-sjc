# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VagasItem(scrapy.Item):
    # define the fields for your item here like:
    vaga = scrapy.Field()
    local = scrapy.Field()
    quantidade = scrapy.Field()
    vaga = scrapy.Field()
    aceita_pcd = scrapy.Field()
    exclusiva_pcd = scrapy.Field()
    escolaridade = scrapy.Field()
    experiencia = scrapy.Field()