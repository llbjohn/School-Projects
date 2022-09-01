
#Student table:
#mysql> CREATE TABLE student (roll int(5) Primary key, name varchar(20) NOT NULL, age int(2) NOT
#NULL, class varchar(3), City varchar(10));
#Fee table:
#mysql> CREATE TABLE fee (roll int(5) references Student(roll), FeeDeposit int(6) NOT NULL, month
#varchar(10));






import os
import platform
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(host='localhost',\
                             user='root',\
                             passwd=' ',\
                             database='School')
mycursor=mydb.cursor()

def stuInsert():                                                           #for inserting student details
    L=[]
    roll=int(input("Enter the roll number : "))                            #taking input from the user(roll no., name, age, class,city) 
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    classs=input("Enter the Class and sec(eg:- 12 A): ")
    L.append(classs)
    city=input("Enter the City of the Student : ")
    L.append(city)
    stud=(L)
    sql="insert into student (roll,name,age,class,city) values (%s,%s,%s,%s,%s)" #command for inserting input into table
    mycursor.execute(sql,stud)
    mydb.commit()

def stuView():                                                              # for viewing student's details
    print("Select the search criteria : ")         
    print("1. Roll")
    print("2. Name")
    print("3. Age")
    print("4. City")
    print("5. All")
    ch=int(input("Enter the choice : "))                                    #in put for search criteria
    if ch==1:
        s=int(input("Enter roll no : "))                                    #searching by student's roll no.
        rl=(s,)
        sql="select * from student where roll=%s"
        mycursor.execute(sql,rl)
    elif ch==2:                                                             #searching by student's name
        s=input("Enter Name : ")
        rl=(s,)
        sql="select * from student where name=%s"
        mycursor.execute(sql,rl)
    elif ch==3:                                                             #searching by student's age
        s=int(input("Enter age : "))
        rl=(s,)
        sql="select * from student where age=%s"
        mycursor.execute(sql,rl)
    elif ch==4:                                                             #searching by student's city
        s=input("Enter City : ")
        rl=(s,)
        sql="select * from student where City=%s"
        mycursor.execute(sql,rl)
    elif ch==5:                                                             #for viewing every students detail
        sql="select * from student"
        mycursor.execute(sql)   
    res=mycursor.fetchall()
    print("The Students details are as follows : ")
    print("(ROll, Name, Age, Class, City)")
    for x in res:
        print(x)
        
def feeDeposit():                                                            #function for depositing fee
    L=[]
    roll=int(input("Enter the roll number : "))                              #taking roll no. of the student whose fee is to be deposited
    L.append(roll)
    feedeposit=int(input("Enter the Fee to be deposited : "))                #fee amount
    L.append(feedeposit)
    month=input("Enter month of fee : ")
    L.append(month)
    fee=(L)
    sql="insert into fee (roll,feeDeposit,Month) values (%s,%s,%s)"
    mycursor.execute(sql,fee)
    mydb.commit()

def feeView():                                                               #function to view students fee details
    print("Please enter the details to view the fee details :")
    roll=int(input("Enter the roll number of the student whose fee is to be viewed : "))
    sql="Select Student.Roll, Student.Name, Student.Class, sum(fee.feeDeposit), fee.month from Student INNER JOIN fee ON Student.roll=fee.roll and fee.roll = %s"
    rl=(roll,)
    mycursor.execute(sql,rl)
    res=mycursor.fetchall()
    print("ROll, Name, Class, Fee Deposited, Month")
    for x in res:
        print(x)
    
    
def removeStu():                                                             #function to remove student's data
    roll=int(input("Enter the roll number of the student to be deleted : ")) #taking roll no. of the student whose data is to be deleted
    rl=(roll,)
    sql="Delete from fee where roll=%s"
    mycursor.execute(sql,rl)
    sql="Delete from Student where roll=%s"
    mycursor.execute(sql,rl)
    mydb.commit()
    print("student data DELETED...")                                          #data deleted message
    

def MenuSet():                                                                #Function For The Student Management System
    print("Enter 1 : To Add Student")
    print("Enter 2 : To View Student ")
    print("Enter 3 : To Deposit Fee ")
    print("Enter 4 : To Remove Student")
    print("Enter 5 : To View Fee of Any Student")
    
    try:                                                                       #Using Exceptions For Validation
        userInput = int(input("Please Select An Above Option: "))              #Taking Input From User
    except ValueError:
        exit("\nHy! That's Not A Number")                                      #Error Message
    else:
        print("\n")                                                            #Print New Line
        if(userInput == 1):
            stuInsert()
        elif (userInput==2):
            stuView()
        elif (userInput==3):
            feeDeposit()
        elif (userInput==4):
            removeStu()
        elif (userInput==5):
            feeView()
        else:
            print("Enter correct choice. . .  ")
            
        
MenuSet()
def runAgain():                                                                 #function asking to run this program again or not
    runAgn = input("\nwant To Run Again Y/n: ")
    while(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        MenuSet()
        runAgn = input("\nwant To Run Again Y/n: ")
        
runAgain()		


