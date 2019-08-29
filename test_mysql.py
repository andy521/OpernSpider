import  pymysql

db = pymysql.connect('localhost', 'root', 'mysql', 'Music')
cursor = db.cursor()
sql = "insert into Music_Score values(default,'1','1','1','1',%s,%s);"% ('2','3')
try:
    cursor.execute(sql)
    db.commit()
    print("插入成功")
except:
    db.rollback()
    print("插入失败")