# -*- coding: UTF-8 -*-
import requests
import time
from lxml import etree
import pymysql
from utiles.to_mysql import insert_data


"""
中国曲谱网爬虫
"""

start_url = 'http://www.qupu123.com'
response = requests.get(start_url)
tree = etree.HTML(response.content)
menu_li = tree.xpath('//div[contains(@class,"menus")]/a/@href')
type_li = []
for m in menu_li:
    u = start_url + m
    type_li.append(u)

