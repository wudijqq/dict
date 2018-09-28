import pymysql
import re


f = open('dict.txt')
db = pymysql.connect('localhost', 'root', '123456', 'dict')

cursor = db.cursor()

for line in f:
    h = re.split(r'\s+', line)
    word = h[0]
    interpret = ' '.join(h[1:])

    sql = "insert into words (word,interpret) \
    values('%s','%s')" % (word, interpret)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.rollback()
f.close()
