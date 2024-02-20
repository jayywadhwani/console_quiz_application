from datetime import datetime
def profile(score,user_name,category):
    temp=datetime.now()
    date,time=str(temp).split(" ")
    a = user_name+'.txt'
    with open(a,'a') as file:
        file.writelines(f"| Your Score is : {str(score)} | Quiz Name : {category} \t| On Date : {date} | On Time : {time} |\n")

def view_profile(user_name):
    a = user_name+'.txt'
    with open(a,'r') as file:
        print(file.read())
