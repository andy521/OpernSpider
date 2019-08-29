# -*- coding: UTF-8 -*-
import requests
import time
from lxml import etree
import pymysql
import logging

"""
中国乐谱网爬虫
"""


def insert_data(music_, name, author, upload_time, source, score_link):
    """
    向mysql插入数据记录
    :return:
    """
    score_link = '"`' + score_link + '`"'
    music_ = '"' + music_ + '"'
    name = '"' + name + '"'
    author = '"' + author + '"'
    upload_time = '"' + upload_time + '"'
    source = '"' + source + '"'
    db = pymysql.connect('localhost', 'root', 'mysql', 'Music')
    cursor = db.cursor()
    sql = """insert into Music_Score values(default,%s,%s,%s,%s,%s,%s);""" % (music_, name, author, upload_time, source, score_link)
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("插入成功")
        time.sleep(0.2)
    except Exception as e:
        print(e)
        db.rollback()
        print("插入失败")


start_url = 'http://www.yuepuwang.com/'
response = requests.get(start_url)
tree = etree.HTML(response.content)
a_li = tree.xpath('//ul[@class="nav"]/li/a')
type_dict = {}
for a in a_li[1:-1]:
    musical_in = a.xpath('./text()')[0]
    link = 'http://www.yuepuwang.com' + a.xpath('./@href')[0]
    type_dict[musical_in] = link
# print(type_dict)
for music_, l_url in type_dict.items():
    b_url = l_url
    while True:
        resp = requests.get(l_url)
        tree_ = etree.HTML(resp.content.decode('utf-8'))
        # print(resp.content.decode('utf-8'))
        if "下页" not in resp.content.decode('utf-8'):
            print('page')
            break
        else:
            tr_list = tree_.xpath("//div[@class='list']/table//tr")[1::]
            for tr in tr_list:
                name = tr.xpath("./td[1]/a//text()")[0]
                score_link = 'http://www.yuepuwang.com' + tr.xpath("./td[1]/a/@href")[0]
                author = tr.xpath('./td[2]/text()')[0]
                upload_time = tr.xpath('./td[4]/small/text()')[0]
                source = tr.xpath('./td[3]/text()')[0]
                insert_data(music_=music_, name=name, author=author, upload_time=upload_time, source=source, score_link=score_link)

            next_page = b_url + tree_.xpath("//a[contains(text(),'下页')]/@href")[0]
            l_url = next_page
            time.sleep(0.5)
