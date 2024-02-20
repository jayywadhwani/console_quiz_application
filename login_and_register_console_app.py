import mysql.connector as my
from datetime import datetime
conn = my.connect(
    host="localhost",
    user="root",
    password="",
    database="questions")
cur = conn.cursor()

def login():
    login_data={}
    user_data = "select * from login_data;"
    cur.execute(user_data)
    data = cur.fetchall()
    for i,j in data:
        login_data[i]=j
    uname=input("Enter your username : ")
    if uname in login_data.keys():
        password=input("Enter your password : ")
        if password in login_data.values():
            print("logged in successfully")
            print(f'Welcome {uname}')
        else:
            print("Wrong password")
            print("Re-enter your password...")
            login()
    else:
        print("Username not found")
        reg= input("Do you wnat to register : Y/N : ").upper()
        if reg in ['Y','YES']:
            print("redricting to registration page \n please wait...")
            register()
        elif reg in ["N","NO"]:
            temp=input("Wanna Login Y/N : ")
            if temp in ['Y','YES']:
                login()
            else:
                exit()
        else:
            print("please select give ans in Y or N")
    return uname,True

def register_data(user_name='Not available'):
    weekDaysMapping = ("Monday", "Tuesday", 
                    "Wednesday", "Thursday",
                    "Friday", "Saturday",
                    "Sunday")
    temp=datetime.now()
    date,time=str(temp).split(" ")
    day= weekDaysMapping[datetime.weekday(temp)]
    register_date_and_time=f"insert into user_register_data values('{user_name}','{day}','{date}','{time}');"
    cur.execute(register_date_and_time)
    conn.commit()

def register():
    login_data={}
    user_data = "select * from login_data;"
    cur.execute(user_data)
    data = cur.fetchall()
    for i,j in data:
        login_data[i]=j
    user_name = input("enter your user name : ")
    if user_name in login_data.keys():
        print("Username already exist ")
        print("redricting to login page \n please wait...")
        login()
    else:
        password=input("Enter your password : ")
        data_saver = f"insert into login_data values('{user_name}','{password}');"
        cur.execute(data_saver)
        conn.commit()
        print("your credentials are saved")
        register_data(user_name)
        login()

def last_login(user_name,week_day):
    temp=datetime.now()
    date,time=str(temp).split(" ")
    day_week= week_day[datetime.weekday(temp)]
    a = user_name+'.txt'
    with open(a,'a') as file:
        file.write(f"\nLast Login On : {day_week} Date and Time : {date} | {time}\n")