from score_console_app import *
def options(explanation,answer,final_score=0):
    opt=input('please select any option from following:').upper()
    if opt==answer:
        print("correct answer : ","\n",explanation,"\n",answer)
    else:
        print("wrong answer correct is ","\n",explanation,"\n",answer)
    score(opt,answer,score_counter)
    for i in score_counter:
        final_score+=i
    print("Your socre is : ",final_score)
    return final_score