import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='ProjectMart')
mycursor=con.cursor()

class Bill:
    def __init__(self):
        print()

    def bill_rec(self,oid,total,disc):
        data=(oid,total,disc)
        sql='insert into bill_record(Order_Id,Total_amount,Discounted_price) values(%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print()

    def bill_display(self):
        c=con.cursor()
        c.execute('select * from bill_record')
        bill_d=c.fetchall()
        print("Bill_No   Oreder_Id  Total_Amount")
        for i in list(bill_d):
            print(str(i[0]).ljust(10),str(i[1]).ljust(11),i[2])