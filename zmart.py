import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='ProjectMart')
mycursor=con.cursor()
sql='alter table userinfo add column Cust_Seller varchar(10);'

mycursor.execute(sql)

