import pymysql as MySQLdb
import pandas as pd

# 连接到MySQL数据库
conn = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    password='admin#1234',
    database='lateral',
    charset='utf8'
)

mysql_page = pd.read_sql("select * from orders", con=conn)

mysql_page.head()