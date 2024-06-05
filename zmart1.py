import pymysql
from zuserinfo import userinfo
from zproduct import product
from zorder import Order
from zpay import paydetail
from zbill import Bill

con=pymysql.connect(host='localhost',user='root',password='',database='ProjectMart')
mycursor=con.cursor()

staff=['st','12']


print("1.Login")
print("2.Signup")
strt=int(input())
admin=0
admin1=0
owner=''
m1=0
conf_ord=0
order1=[]
quan=[]  
bill_1=Bill()

#login
while strt==1:
    user=input('Username: ')
    password=input('Password: ')
    b1=userinfo()
    if user == staff[0] and password == staff[1]:
        admin1=1
        print('welcome')
        break
    elif b1.login(user,password):
        m1=1
        break

    else:
        print('Invalid user ID')
    print('1 to exit')
    if input()=='1':
        break
        
#signup
if strt==2:
    a1=userinfo()
    m1=1
    F_name=input('First Name : ')
    L_name=input('Last Name  : ')
    Email_ID=input('Email ID   : ')
    while True:
        User_name=input('User Name  : ')
        if a1.chk_user(User_name):
            print('Username aldready exist')
        else:
            break   
    Password=input('Password   : ')
    Addres=input('Address    : ')
    Ph=int(input('Phone no.  : '))
    brs=input('Buyer (B) or Seller (S)')
    if a1.insert(F_name,L_name,Email_ID,User_name,Password,Addres,Ph,brs):
        admin=1

if admin1==1:
    print('1.Sell Product\n2.Buy Product\n3.Bill Records')
    owner=input()

#admin user
while admin==1 or owner=='1' or b1.buying==1:
    print('*********************')
    print('1.Add items')
    print('2.Add discount coup')
    print('3.Delete item')
    print('4.Exit')
    print('select the process')
    admsel=int(input())

    #add item
    if admsel==1:
        pid=input('pid :')
        pname=input('pname :')
        pcategory=input('pcategory :')
        pprice=input('pprice :')
        disc_id=input('disc id :')
        adm=product()
        adm.insert_prod(pid,pname,pcategory,pprice,disc_id)
    
    #add discount
    if admsel==2:
        disc_id=input("Disc ID ")
        disc_per=int(input('Enter the percentage'))
        adm=product()
        adm.add_disc_coup(disc_id,disc_per)

    #delete item
    if admsel==3:
        itm_id=input()
        adm=product()
        adm.del_prod(itm_id)


    if  admsel==4:
        break

#product purchase 
while m1==1 or owner=='2' or b1.buying==1:
    a2=product()
    a3=Order()
    print('1.View Product')
    print('2.Purchase items')
    print('3.Confirm Purchase')
    print('4.Filter category')
    print('5.Exit')
    print('6.View order')
    print('*******************')
    ex=input('Select :')
    print('*******************')

    #view product
    if ex=='1':
        print()
        a2.list_of_products()

    #add item
    while ex=='2':
        x=input('Prod id')
        y=input('Quantity')
        order1.append(x)
        quan.append(y)
        print('1 to exit \n2.Countinue')
        chod=input()
        if chod=='1':
            break

    #Purchase confirm
    if ex=='3':
        conf_ord=1
        break

    #filter categree
    if ex=='4':
        cat=input('Type the categry that you want to : ')
        a3.filter_prod(cat)
    
    #view ordered item
    if ex=='6':
        if len(order1)<=0:
            print('empty')
        else:
            for i,a in enumerate(order1):
                print(a.ljust(7),quan[i])
        
    #exit
    if ex=='5':
        break

#Confirming order
pay=0
if len(order1)>0 and conf_ord==1:
    print('*****************')
    for i,a in enumerate(order1):
        print(a.ljust(7),quan[i])
    while True:
        print('1.Delete product from cart')
        print('2.Proceede to pay')
        del_ord=input()
        #del order
        if del_ord=='1':
            print('Type the Pid that u want to cancel')
            cance=input()
            a3.cancel_order(cance,order1,quan)

        #Proceed to pay
        elif del_ord=='2':
            pay=1
            print('Enter The discount Id\nElse Press Enter')
            disc=input()
            a3.order_item(order1,quan,b1.u_id,disc)
            break

elif len(order1)==0 and conf_ord==1:
    print('Empty cart')

#pay method
delivery=0
if pay==1:
    print('----------------------------')
    print('Total Amount:    Discount Price')
    print(a3.total,'     ',a3.disc_price)
    print('----------------------------')
    pa1=paydetail()
    pa1.pay_method()
    print('order placed successfully')
    bill_1.bill_rec(a3.o_id,a3.total,a3.disc_price)
    delivery=1

if delivery==1:
    print('1.If change delivery Address\nElse press ENTER')
    addr=input()
    if addr==1:
        adres=input("Typr the address")
    print('************************************')
    print(" Order will be delever 30-02-2024")
    print('            (+_+)')
    print('        Tq for shopping')
    print("************************************")


if owner=='3':
    bill_1.bill_display()