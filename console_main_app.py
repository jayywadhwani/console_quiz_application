from login_and_register_console_app import *
from clear_terminal_console_app import *
from profile_user_console_app import *
from options_console_app import *
import mysql.connector as my

conn = my.connect(
    host="localhost",
    user="root",
    password="",
    database="questions")

weekDaysMapping = ("Monday", "Tuesday", 
                   "Wednesday", "Thursday",
                   "Friday", "Saturday",
                   "Sunday")

temp_uname,temp_login_detect=login()
# Detects user last login
if temp_login_detect==True:
    last_login(temp_uname,weekDaysMapping)

while True:
    temp_counter=0
    choice = input(f"Hello {temp_uname} what you want to do\n 1. Play Quiz or \n 2. View Profile \n 3. Exit \n Your input : ").lower()
    if choice=='1':
        while True:
            table_name =input("which quiz you want to play "+"\n"+ "1. PYTHON"+"\n"+"2. JAVA"+"\n"+"3. CPP"+"\n").lower()
            if table_name=='1' or table_name=='python':
                table_name='py_que'
                category="PYTHON"
            if table_name=='2' or table_name=='java':
                table_name='java_que'
                category="JAVA"
            if table_name=='3' or table_name in ['cpp','c++']:
                table_name='cpp_que'
                category="C++"
            
            que = f"select serial_no,question,op_1,op_2,op_3,op_4 from {table_name};"
            cur.execute(que)
            data = cur.fetchall()
            counter=1
            for i in data:
                serial_no, question, op_1, op_2, op_3, op_4 = i
                print(serial_no, question, "\n", op_1, "\n",
                    op_2, "\n", op_3, "\n", op_4, "\n")
                ans = f"select explanation,answer from {table_name} where serial_no={counter};"
                cur.execute(ans)
                data = cur.fetchall()
                for i in data:
                    explanation,answer = i
                    temp_score=options(explanation,answer)
                    counter+=1

            again=input("Do you want to play again (Y/N): ").lower()
            if again in ['y','yes']:
                profile(temp_score,temp_uname,category)
                try:
                    score_counter.pop(temp_counter)
                    temp_counter+=1
                except IndexError as e:
                    print("some error Occured")
                finally:
                    temp_counter-=1
            if again in ['n','no']:
                temp=input("Do you want to exit quiz (Y/N): ").lower()
                if temp in ['y','yes']:
                    profile(temp_score,temp_uname,category)
                    clear_screen()
                    break
                else:
                    print("please select input")

    if choice=='2':
        view_profile(temp_uname)
        clear_screen()
    
    if choice=='3':
        clear_screen()
        exit()