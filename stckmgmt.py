import os
import mysql.connector as sqltor
import datetime
now=datetime.datetime.now()

def create_tables():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    
    print('Creating PRODUCT table...')
    st1="CREATE TABLE if not exists PRODUCT ( Pcode integer(4) PRIMARY KEY, Pname char(40) NOT NULL, Pprice integer(5) ,Pqty integer(4) ,Pcat char(30));"
    cursor.execute(st1)
    
    print('Creating ORDER table...')
    st2="CREATE TABLE if not exists ORDERS ( OrderId integer(4) PRIMARY KEY,Orderdate DATE,Pcode char(40) references PRODUCT(Pcode),Pprice integer(8),Pqty int(4),Supplier char(50),Pcat char(30));"
    cursor.execute(st2)
    
    print('Creating SALES table...')
    st3="CREATE TABLE if not exists SALES ( SalesId integer(4) PRIMARY KEY,Salesdate DATE,Pcode char(40) references PRODUCT(Pcode),Pprice integer(8),Pqty int(4),Total integer(10));"
    cursor.execute(st3)

    print('Creating USER table...')
    st4="CREATE TABLE if not exists USER ( UId char(20) PRIMARY KEY,Uname char(30) NOT NULL,Upwd char(30));"
    cursor.execute(st4)

    print('Tables created...!')

def search_tables():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='show tables;'
    cursor.execute(sql)
    for i in cursor:
        print(i)

def add_product():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='INSERT INTO PRODUCT(Pcode,Pname,Pprice,Pqty,Pcat) values(%s,%s,%s,%s,%s)'
    code=int(input('\t\t Enter product code:'))
    search='SELECT COUNT(*) FROM PRODUCT WHERE Pcode=%s;'
    val=(code,)
    cursor.execute(search,val)
    for x in cursor:
        ray=x[0]
    if ray==0:
        name=input('\t\t Enter product name:')
        qty=int(input('\t\t Enter product quantity:'))
        price=int(input('\t\t Enter product unit price:'))
        cat=input('\t\t Enter product category:')
        val=(code,name,price,qty,cat)
        cursor.execute(sql,val)
        mycon.commit()
        print('\t\t*******************')
        print('\t\t Product added...!')
        print('\t\t*******************') 
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product already exist.!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')

def update_a():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    code=int(input('\t\t Enter product code:'))
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if code in ray: 
        name=input('\t\t Enter new name:')
        sql1='UPDATE PRODUCT SET Pname=%s WHERE Pcode=%s;'
        val=(name,code)
        cursor.execute(sql1,val)
        mycon.commit()
        print('\t\t******************')
        print('\t\t Name updated...!')
        print('\t\t******************')
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')

def update_b():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    code=int(input('\t\t Enter product code:'))
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if code in ray:
        price=int(input('\t\t Enter new price:'))
        sql='UPDATE PRODUCT SET Pprice=%s WHERE Pcode=%s;'
        val=(price,code)
        cursor.execute(sql,val)
        mycon.commit()
        print('\t\t*******************') 
        print('\t\t Price updated...!')
        print('\t\t*******************')
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
    
def update_c():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    code=int(input('\t\t Enter product code:'))
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if code in ray:
        qty=input('\t\t Enter quantity to be added:')
        sql='UPDATE PRODUCT SET Pqty=Pqty+%s WHERE Pcode=%s;'
        val=(qty,code)
        cursor.execute(sql,val)
        mycon.commit()
        print('\t\t**********************')
        print('\t\t Quantity updated...!')
        print('\t\t**********************')
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')

def update_d():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    code=int(input('\t\t Enter product code:'))
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if code in ray:
        cat=input('\t\t Enter new category:')
        sql='UPDATE PRODUCT SET Pcat=%s WHERE Pcode=%s;'
        val=(cat,code)
        cursor.execute(sql,val)
        mycon.commit()
        print('\t\t**********************')
        print('\t\t Category updated...!')
        print('\t\t**********************')
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!') 

def delete_product():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    code=int(input('\t\t Enter product code:'))
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if code in ray:
        sql='DELETE FROM PRODUCT WHERE Pcode=%s;'
        val=(code,)
        cursor.execute(sql,val)
        mycon.commit()
        print(cursor.rowcount,'record(s) deleted')
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!') 

def list_product():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT*FROM PRODUCT;'
    cursor.execute(sql)
    print('\t\t\t\t PRODUCT DETAILS')
    print('-'*133)
    print('\t\t Code \t Name \t Price \t Quantity \t Category')
    print('-'*133)
    for i in cursor:
        print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
    print('-'*133)

def list_prcode(code):
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if code in ray:
        sql1='SELECT*FROM PRODUCT WHERE Pcode=%s;'
        val=(code,)
        cursor.execute(sql1,val)
        print('\t\t\t\t PRODUCT DETAILS')
        print('-'*133)
        print('\t\t Code \t Name \t Price \t Quantity \t Category')
        print('-'*133)
        for i in cursor:
            print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
        print('-'*133)
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Product does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!')

def list_prcat(cat):
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT * FROM PRODUCT;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[4]]
    if cat in ray:
        sql='SELECT*FROM PRODUCT WHERE Pcat=%s;'
        val=(cat,)
        cursor.execute(sql,val)
        print('\t\t\t\t PRODUCT DETAILS')
        print('-'*133)
        print('\t\t Code \t Name \t Price \t Quantity \t Category')
        print('-'*133)
        for i in cursor:
            print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4])
        print('-'*133)
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Category does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def add_order():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='INSERT INTO ORDERS(OrderId,Orderdate,Pcode,Pprice,Pqty,Supplier,Pcat) values (%s,%s,%s,%s,%s,%s,%s)'
    code=int(input('\t\t Enter product code:'))
    oid=now.year+now.month+now.day+now.hour+now.minute+now.second
    qty=int(input('\t\t Enter product quantity:'))
    price=int(input('\t\t Enter product unit price:'))
    cat=input('\t\t Enter product category:')
    supplier=input('\t\t Enter supplier details:')
    val=(oid,now,code,price,qty,supplier,cat)
    cursor.execute(sql,val)
    mycon.commit()
    print('\t\t******************')
    print('\t\t Order added...!')
    print('\t\t******************') 

def list_order():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT*FROM ORDERS;'
    cursor.execute(sql)
    print('\t\t\t\t ORDER DETAILS')
    print('-'*133)
    print('\t\t OrderId \t Date \t Pcode \t Pprice\tPqty \t Supplier \t Pcat')
    print('-'*133)
    for i in cursor:
        print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
    print('-'*133)

def list_orid(Id):
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT * FROM ORDERS;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if Id in ray:
        sql='SELECT*FROM ORDERS WHERE OrderId=%s;'
        val=(Id,)
        cursor.execute(sql,val)
        print('\t\t\t\t ORDER DETAILS')
        print('-'*133)
        print('\t\t OrderId \t Date \t Pcode \t Pprice\tPqty \t Supplier \t Pcat')
        print('-'*133)
        for i in cursor:
            print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
        print('-'*133)
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Order does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!')

def list_orsupl(sup):
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT * FROM ORDERS;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[5]]
    if sup in ray:
        sql='SELECT*FROM ORDERS WHERE Supplier=%s;'
        val=(sup,)
        cursor.execute(sql,val)
        print('\t\t\t\t ORDER DETAILS')
        print('-'*133)
        print('\t\t OrderId \t Date \t Pcode \t Pprice\tPqty \t Supplier \t Pcat')
        print('-'*133)
        for i in cursor:
            print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
        print('-'*133)
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Supplier does not exist!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def sales_product():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    code=int(input('\t\t Enter product code:'))
    sql='SELECT * FROM PRODUCT WHERE Pcode=%s;'
    val=(code,)
    cursor.execute(sql,val)
    for x in cursor:
        ray=x[0]
        if ray==code:
            sql='SELECT*FROM PRODUCT WHERE Pcode=%s;'
            val=(code,)
            cursor.execute(sql,val)
            for x in cursor:
                print('\t\t --Product details--')
                print('\t\t (Pcode,Pname,Pprice,Pqty,Pcat)')
                print('\t\t',x)
                price=int(x[2])
                pqty=int(x[3])
            qty=int(input('\t\t Enter quantity:'))
            if qty<=pqty:
                total=qty*price
                sql1='INSERT INTO SALES(SalesId,Salesdate,Pcode,Pprice,Pqty,Total)values(%s,%s,%s,%s,%s,%s);'
                now=datetime.datetime.now()
                Id=int(ray)+now.month+now.day+now.hour+now.minute+now.second 
                val1=(Id,now,code,price,qty,total)
                cursor.execute(sql1,val1)
                sql2='UPDATE PRODUCT SET Pqty=Pqty-%s WHERE Pcode=%s'
                val2=(qty,code)
                cursor.execute(sql2,val2)
                mycon.commit()
                print('\t\t******************')
                print('\t\t Record added...!')
                print('\t\t******************')
            else:
                print('\t\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print('\t\t Sorry, Quantity not available')
                print('\t\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        else:
            print('\t\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!') 
            print('\t\t Sorry, Product not available')
            print('\t\t !!!!!!!!!!!!!!!!!!!!!!!!!!!!!') 
            
def list_sales():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT*FROM SALES;'
    cursor.execute(sql)
    print('\t\t\t\t SALES DETAILS')
    print('-'*133)
    print('\t\t SalesId Salesdate\tPcode  Pprice\tPqty\tTotal')
    print('-'*133)
    for i in cursor:
        print('\t\t',i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5])
    print('-'*133)

def add_user():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    uid=input('\t\t Enter email id:')
    name=input('\t\t Enter name:')
    passwd=input('\t\t Enter password:')
    sql='INSERT INTO USER(UId,Uname,Upwd) values (%s,%s,%s);'
    val=(uid,name,passwd)
    cursor.execute(sql,val)
    mycon.commit()
    print('\t\t*****************') 
    print('\t\t User added...!')
    print('\t\t*****************')

def list_user():
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT UId, Uname FROM USER;'
    cursor.execute(sql)
    print('\t\t\t\t USER DETAILS')
    print('-'*133)
    print('\t\t UserId \t\t Uname')
    print('-'*133)
    for i in cursor:
        print('\t\t',i[0],'\t',i[1])
    print('-'*133)

def list_userid(Id):
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT * FROM USER;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if Id in ray:
        sql='SELECT UId,Uname FROM USER WHERE UId=%s;'
        val=(Id,)
        cursor.execute(sql,val)
        print('\t\t\t\t USER DETAILS')
        print('-'*133)
        print('\t\t UserId \t\t Uname')
        print('-'*133)
        for i in cursor:
            print('\t\t',i[0],'\t',i[1])
        print('-'*133)
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!')
        print('\t\t Invalid user id!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!')

def list_userpwd(Id):
    mycon=sqltor.connect(host='localhost',user='root',passwd='abcd',database='stock')
    cursor=mycon.cursor()
    sql='SELECT * FROM USER;'
    cursor.execute(sql)
    ray=[]
    for x in cursor:
        ray+=[x[0]]
    if Id in ray:
        sql='SELECT*FROM USER WHERE UId=%s;'
        val=(Id,)
        cursor.execute(sql,val)
        print('\t\t\t\t USER DETAILS')
        print('-'*133)
        print('\t\t UserId \t\t Uname \t\t Upwd')
        print('-'*133)
        for i in cursor:
            print('\t\t',i[0],'\t',i[1],'\t',i[2])
        print('-'*133)
    else:
        print('\t\t!!!!!!!!!!!!!!!!!!!!')
        print('\t\t Invalid user id!!')
        print('\t\t!!!!!!!!!!!!!!!!!!!!')
               
def product_mgmt():
    while True:
        print('\t\t--------------------------') 
        print("\t\t 1. Add New  Product")
        print("\t\t 2. List Product")
        print("\t\t 3. Update Product")
        print("\t\t 4. Delete Product")
        print("\t\t 5. Back (MAIN MENU)")
        print('\t\t-------------------------')
        p=int(input("\t\t Enter your Choice:"))
        if p==1:
            add_product()
        if p==2:
            print('\t\t\t-------------------------------')
            print('\t\t\t a. List all products')
            print('\t\t\t b. List product code wise')
            print('\t\t\t c. List product category wise')
            print('\t\t\t d. Back(Main Menu)')
            print('\t\t\t-------------------------------')
            p=(input('\t\t Enter your choice:'))
            if p in 'aA':
                list_product()
            if p in 'bB':
                code=int(input('\t\t Enter product code:'))
                list_prcode(code)
            if p in 'cC':
                cat=input('\t\t Enter product category:')
                list_prcat(cat)
            if p in 'dD':
                break 
        if p==3:
            print('\t\t\t-----------------------')
            print('\t\t\t a. Update name')
            print('\t\t\t b. Update price')
            print('\t\t\t c. Update quantity')
            print('\t\t\t d. Update category')
            print('\t\t\t e. Back(Main Menu)')
            print('\t\t\t-----------------------')
            p=input('\t\t Enter your choice:')
            if p in 'aA':
                update_a()
            if p in 'bB':
                update_b()
            if p in 'cC':
                update_c()
            if p in 'dD':
                update_d()
            if p in 'eE':
                break
                
        if p==4:
            delete_product()
        if p==5:
            break        

def purchase_mgmt():
    while True:
        print('\t\t----------------------------')
        print("\t\t 1. Add Order")
        print("\t\t 2. List Order")
        print("\t\t 3. Back (MAIN MENU)")
        print('\t\t----------------------------')
        p=int(input("\t\t Enter your Choice:"))
        if p==1:
            add_order()
        elif p==2:
            print('\t\t\t---------------------------------')
            print('\t\t\t a. List all orders')
            print('\t\t\t b. List order id wise')
            print('\t\t\t c. List order supplier wise')
            print('\t\t\t d. Back(Main Menu)')
            print('\t\t\t---------------------------------')
            p=input('\t\t Enter your choice:')
            if p in 'aA':
                list_order()
            if p in 'bB':
                Id=int(input('\t\t Enter order id:'))
                list_orid(Id)
            if p in 'cC':
                sup=input('\t\t Enter supplier details:')
                list_orsupl(sup)
            if p in 'dD':
                break
        elif p==3:
            break

def sales_mgmt():
    while True:
        print('\t\t---------------------------') 
        print("\t\t 1. Sales Items")
        print("\t\t 2. List Sales")
        print("\t\t 3. Back (MAIN MENU)")
        print('\t\t---------------------------')
        p=int(input("\t\t Enter your Choice:"))
        if p==1:
            sales_product()
        if p==2:
            list_sales()
        if p==3:
            break

def user_mgmt():
    while True:
        print('\t\t-----------------------------')
        print("\t\t 1. Add User")
        print("\t\t 2. List User")
        print("\t\t 3. Back (MAIN MENU)")
        print('\t\t-----------------------------') 
        p=int(input("\t\t Enter your Choice:"))
        if p==1:
            add_user()
        if p==2:
            print('\t\t\t-------------------------------') 
            print('\t\t\t a. List all user')
            print('\t\t\t b. List user id wise')
            print('\t\t\t c. List user with password')
            print('\t\t\t d. Back(Main Menu)')
            print('\t\t\t-------------------------------')
            p=input('\t\t Enter your choice:')
            if p in 'aA':
                list_user()
            if p in 'bB':
                Id=input('\t\t Enter email id:')
                list_userid(Id)
            if p in 'cC':
                Id=input('\t\t Enter email id:')
                list_userpwd(Id)
            if p in 'dD':
                break
        if p==3:
            break

def db_mgmt():
    while True:
        print('\t\t---------------------------')
        print('\t\t 1. Table Creation')
        print('\t\t 2. List Tables')
        print('\t\t 3. Back(Main Menu)')
        print('\t\t---------------------------')
        p=int(input('Enter your choice:'))
        if p==1:
            create_tables()
        if p==2:
            search_tables()
        if p==3:
            break

	
print('-'*133)    
print('\t\t\t\t\t\t','*'*10, 'HELLO!!!', '*'*10)
print('-'*133)
a=input('Enter mysql username:')
b=input('Enter mysql password:')

if a=='root' and b=='abcd':
    print('Congrats!! Your MySQL connection established..')
    print('\n\tNote: Please setup database if using for first time, else ignore :)')
    while True:
        print('-'*133)
        print('\t\t\t*****************')
        print('\t\t\t STOCK MANAGEMENT')
        print('\t\t\t*****************')
        print('\t\t 1. PRODUCT MANAGEMENT')
        print('\t\t 2. PURCHASE MANAGEMENT')
        print('\t\t 3. SALES MANAGEMENT')
        print('\t\t 4. USER MANAGEMENT')
        print('\t\t 5. DATABASE SETUP')
        print('\t\t 6. EXIT \n')
        print('-'*133)
        num=int(input('Enter your choice:'))
        if num==1:
            product_mgmt()
        if num==2:
            purchase_mgmt()
        if num==3:
            sales_mgmt()
        if num==4:
            user_mgmt()
        if num==5:
            db_mgmt()
        if num==6:
            print('\t\t\t\t\t\t *****************************')
            print('\t\t\t\t\t\t    THANK YOU FOR VISITING!!')
            print('\t\t\t\t\t\t *****************************')
            break
else:
    print('\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('\t INVALID USERNAME OR PASSWORD!!!')
    print('\t TRY AGAIN')
    print('\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
