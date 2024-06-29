import random
'''
1 for rock ✊
-1 for paper 🖐
0 for scissors ✌️
'''
computer = random.choice([-1,0,1])
you = input("Nhập lựa chọn của bạn:\nr for Rock ✊\np for Paper 🖐\ns for Scissors ✌️\n")
dic = {"r":1 ,"p":-1, "s":0}
choice = dic[you]
reverseDic = {1:"Rock", -1:"Paper", 0:"Scissors"}
print(f"You choose {reverseDic[choice]} and Computer choose {reverseDic[computer]}")
if(computer == choice):
    print("Hòa!")
else:
    if(computer == -1 and choice == 1):
        print("You Lose!")
    elif(computer == -1 and choice == 0):
        print("You Win!")
    elif(computer == 1 and choice == -1):
        print("You Win!")
    elif(computer == 1 and choice == 0):
        print("You Lose!")
    elif(computer == 0 and choice == 1):
        print("You Win!")
    elif(computer == 0 and choice == -1):
        print("You lose!")
    else:
        print("Something went wrong")