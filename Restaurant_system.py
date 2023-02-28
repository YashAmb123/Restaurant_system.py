# Connecting MYSQL Database

import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="Yash_@1902")

# Selecting or Creating database

c = con.cursor()
sql="use Restaurant"
c.execute(sql)

# Function For Signing-in into System

def login():
    print("\n")
    print("_______________<<<<< Welcome to Indian Restaurant >>>>>_______________")
    print("\n")
    p=input("System Password: ")
    if p == "123456":
        Show_Options()
    else:
        login()

# Showing Options list

def Show_Options():
    print(" 1-Foods\n 2-Shef\n 3-Show_Salary\n 4-New_Order\n 5-Show_Total_Income\n 6-Show_Bills   ")
    choice=input("Choose one option: ")
    if(choice=='1'):
        Food()
    elif(choice=='2'):
        Shef()
    elif(choice=='3'):
        Show_Salary()
    elif(choice=='4'):
        New_order()
    elif(choice=='5'):
        Total_Income()
    elif(choice=='6'):
        Expenditure()
    else:
        print("Entered Wrong Option Try again!!!....")
        Show_Options()

# Creating Foods Function

def Food():
    choice=input("1-Add   2-Remove   3-Display   4-Main_Menu:")
    if choice == '1':
        Food_name=input("Enter Food Name: ")
        Food_Price=input("Enter Food Price: ")
        Self=input("Whom did you like Prepared by: ")
        Food_id=input("Enter Food_ID: ")
        data=(Food_name,Food_Price,Self,Food_id)
        sql="insert into Food values(%s,%s,%s,%s)"
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Inserted Successfully")
        Show_Options()
    elif choice=='2':
        Food_id=input("Food ID: ")
        data=(Food_id,)
        sql="delete from Food where foodid=%s"
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Removed Successfully")
        Show_Options()
    elif choice=='3':
        sql="select * from Food"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print("Food_Name: ",i[0])
            print("Food_Price: ",i[1])
            print("Shef_Name: ",i[2])
            print("Food_ID: ",i[3])
        print("Data Fetched Successfully.............")
        Show_Options()
    else:
        Show_Options()

def FoodID():
    sql="select count(*),max(FoodID) from Foods"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        if i[0] == 0:
            return(1)
        else:
            return int((i[1])+1)
        
def Shef_name():
    sql="select name,foods from shef"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i[0],"-",i[1])
    return

#Inserting or Deleting Cook

def Shef():
    choice=input("1-Insert   2-Delete  3-Show   4-Show options: ")
    if choice=='1':
        Shef_name=input("Enter Shef Name: ")
        Shef_ID=input("Enter ID: ")
        Foods=input("Enter Foods: ")
        Salary=int(input("Enter Salary to be given: "))
        doj=input("Date of joining: D/M/Y: ")
        data=(Shef_name,Shef_ID,Foods,Salary,doj)
        sql="insert into Shef values(%s,%s,%s,%s,%s)"
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Inserted Successfully")
        Show_Options()
    elif choice=='2':
        Shef_name=input("Enter Shef Name: ")
        Shef_ID=input("Aadhar: ")
        data=(Shef_name,Shef_ID)
        sql="delete from shef where Shef_Name=%s and Self_ID=%s"
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Removed Successfully")
        Show_Options()
    elif choice=='3':
        sql="select * from Shef"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i[0],"-",i[1],"-",i[2],"-",i[3],"-",i[4])
        print("\n")
    else:
        Show_Options()

# Paying Shef Salary

def Show_Salary():
    sql="select * from Shef"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i[0],"-",i[1],"-",i[2],"-",i[3],"-",i[4])
        print("--------------------------------")
    Shef_name=input("Enter Shef Name: ")
    date=input("Date: D/M/Y: ")
    Salary=int(input("Enter Salary per month: "))
    Working_Months=int(input("Enter Working_months in year: "))
    Total_Salary=Salary*Working_Months
    data=(Shef_name,date,Salary,Working_Months,Total_Salary)
    sql="Insert into salary values(%s,%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Total Salary: ",Total_Salary,"Rs ")
    print("_______________________________________")
    Show=input("1-Show_Salary    2-Show_Options  ")
    if Show =='1':
        Show_Salary()
    else:
        Show_Options()

#Adding New Order

def New_order():
    option=input("Select 1-Add_order  2-Delete_Order  3-Show_Orders: ")
    if option=='1':
        c=con.cursor()
        Food_ID=input("Enter Food ID: ")
        Price=input("Enter Food Price: ")
        Date=input("Enter Date of order in D/M/Y: ")
        Customer_Name=input("Enter Customer Name: ")
        data=(Food_ID,Price,Date,Customer_Name)
        sql="insert into orders values(%s,%s,%s,%s)"
        c.execute(sql,data)
        con.commit()
        print("Data Inserted Successfully.............")
        Show_Options()
    elif option=='2':
        c=con.cursor()
        Food_ID=input("Enter Food ID: ")
        data=(Food_ID,)
        sql="Delete orders where foodids=%s"
        c.execute(sql,data)
        con.commit()
        print("Data Removed Succcessfully..........")
        Show_Options()
    elif option=='3':
        sql="select * from orders"
        c=con.cursor()
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print("Order_ID: ",i[0])
            print("Order_Price: ",i[1])
            print("Order_Date: ",i[2])
            print("Customer_Name: ",i[3])
        print("All Orders Fetched Successfully..........")
    else:
        Show_Options()

# Monthly net income

def Total_Income():
    c=con.cursor()
    t=input("1-All   2-Year    3-Show Options")
    if t=='1':
        sql="select price from orders"
        c.execute(sql)
        d=c.fetchall()
        Order_Income=0
        for i in d:
            Order_Income+=i[0]
        print("Total Income from Orders:",Order_Income,"Rs")
    elif t=='2':
        y=input("Enter Year: ")
        sql="select Price,date from orders"
        c.execute(sql)
        d=c.fetchall()
        Order_Income=0
        for i in d:
            if y in i[1]:
                Order_Income+=i[0]
        print("Total Income from Orders:",Order_Income,"Rs")
    else:
        Show_Options()

#Making New Expenditure

def Expenditure():
    options=input("1-Bill Entry   2-Show Bills   3-Show Options: ")
    if options=='1':
        type=input("Enter Type: ")
        Price=input("Enter Price: ")
        Date=input("Enter date:D/M/Y ")
        data=(type,Price,Date)
        sql="insert into Expenditure values(%s,%s,%s)"
        c=con.cursor()
        c.execute(sql,data)
        con.commit()
        print("Data Inserted Successfully")
        Show_Options()
    elif options=='2':
        c=con.cursor()
        sql="select * from expenditure"
        c.execute(sql)
        d=c.fetchall()
        for i in d:
            print(i)
    else:
        Show_Options()

login()




        
        




