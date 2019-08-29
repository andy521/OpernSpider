import pymysql
import time


def insert_data(music_, name, author, upload_time, source, score_link, uploader, player):
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
    uploader = '"' + uploader + '"'
    player = '"' + player + '"'
    db = pymysql.connect('localhost', 'root', 'mysql', 'Music')
    cursor = db.cursor()
    sql = """insert into Music_Score values(default,%s,%s,%s,%s,%s,%s);""" % (
    music_, name, uploader, upload_time, source, score_link, player, author)
    # print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("插入成功")
        time.sleep(0.1)
    except Exception as e:
        print(e)
        db.rollback()
        print("插入失败")
