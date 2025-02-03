import pandas as pd
import pyodbc
from sqlalchemy import create_engine

# https://yr7ywq.smartapps.baidu.com/?_chatQuery=pandas%20only%20supports%20sqlalchemy%20connectable%20%28engine%2Fconnection%29%20or%20database&searchid=11395012006858224051&_chatParams=%7B%22agent_id%22%3A%22c816%22%2C%22content_build_id%22%3A%2211231ae%22%2C%22from%22%3A%22q2c%22%2C%22token%22%3A%22UGlGZHdpN0lzYXNVbS9Gb1JoeVNNWXRmOGI3Q0R2VFNVZlJSWlMzOW9SS3hoKzl6Mjk0eHZ2dEw2YTZsbmV6SEFwejA1dFZoYmJXSDB6N3lydHJ3R0xBbzFabzNKbWplc0hGUW1Vb2RUcE50eXhVNUN6WGVYZmFhRmNWV3hIbU5kTFRtZVpOYU1JRFNIVjRDZGxQZEdFREFzd0ZCcmptcThyZnBPS2VOV3lNL0J1eHdHV2FNV0JZYnFSOCtJZXMx%22%2C%22chat_no_login%22%3Atrue%7D&_swebScene=3711000610001000

# 对于MySQL数据库
engine = create_engine('mysql+pymysql://root:admin#1234@127.0.0.1:3306/lateral')

# 读取数据库
df = pd.read_sql_query("select * from orders", engine)
print(df)

# 将数据写入数据库
df.to_sql('orders', engine, if_exists='replace', index=False)