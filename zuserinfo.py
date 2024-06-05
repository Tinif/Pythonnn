
import pymysql

con=pymysql.connect(host='localhost',user='root',password='',database='ProjectMart')
mycursor=con.cursor()

class userinfo:
    def __init__(self):
        print('*******************************')

    def insert(self,fname,lname,email,username,password,address,ph,brs):
        
        self.fname=fname
        self.lname=lname
        self.email=email
        self.username=username
        self.password=password
        self.address=address
        self.ph=ph
        self.brs=brs

        data=(self,self.email,self.username,self.password,self.fname,self.lname,self.address,self.ph,self.brs)
        sql='insert into userinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        if brs=='B':
            return True

        print('Successfully Created')

    def chk_user(self,User_name):
        data=User_name
        c=con.cursor()
        c.execute('select username from userinfo where username = %s',data)
        data=c.fetchall()
        for i in list(data):
            if User_name in i:               
                return True
            else:
                print(i)
                return False



    def login(self,user,password):
        self.user=user
        self.password=password
        data=self.user
        c=con.cursor()
        c.execute('select * from userinfo where username = %s',data)
        data=c.fetchall()
        if len(data)==0:
            return False
        self.buying=0
        if self.password in data[0]:
            self.u_id=data[0][0]
            print('Login Successfully')
            if data[0][8]=='B':
                self.buying=1
                return True
            else:
                return True

