import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='ProjectMart')
mycursor=con.cursor()

c=con.cursor()
c.execute('select prod_id,Prod_name,Price from product')
#the prod ID available
dat=c.fetchall()
pid_ck=[]
for i in dat:
    pid_ck.append(i[0])

#id
c=con.cursor()
c.execute('select max(Them_the) from order_item')
nom=c.fetchall()
#disc Id
c.execute('select * from discount')
discount=c.fetchall()
d=[]
dp=[]
for i in discount:
    d.append(i[0])
    dp.append(i[1])



class Order:
    def __init__(self):
        print('****************************')


    def filter_prod(self,cat):
        c=con.cursor()
        c.execute('select prod_id,Prod_name,Price from product where category= %s',cat)
        data=c.fetchall()
        print('Pid   Pname  Price')
        for i in list(data):
            print(*i)
    
    def cancel_order(self,cance,order1,quan):
        if cance in order1:
            c1=order1.index(cance)
            c2=quan[c1]
            order1.remove(cance)
            quan.pop(c1)
    
    #order item
    def order_item(self,order1,quan,u_id,disc):
        total=0
        for i,a in enumerate(order1):
            if a in pid_ck:
                c=con.cursor()
                c.execute('select price from product where prod_id = %s',a)
                p_price=c.fetchall()


                data=(str(nom[0][0])+'K'+str(u_id),a,p_price[0][0],quan[i],float(quan[i])*p_price[0][0])
                sql='insert into order_item(order_id,Product_id,prod_price,quantity,subTotal) values(%s,%s,%s,%s,%s)'
                c=con.cursor()
                c.execute(sql,data)
                con.commit()
                self.o_id=str(nom[0][0])+'K'+str(u_id)
                total+=float(quan[i])*p_price[0][0]
        self.total=total
        self.disc_price=total
        if disc in d:
            ind=d.index(disc)
            discp=dp[ind]
            self.disc_price=total*discp

        print('the')


