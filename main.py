
import random

computer_choice = random.choice([-1,0,1])
user_choice = input("Enter your choice : ")

userDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

user = userDict[user_choice]

print(f"You chose {reverseDict[user]}\nComputer chose {reverseDict[computer_choice]}")

if(computer_choice == user):
    print("Its a draw")

else:
    if(computer_choice == -1 and user == 1):
        print("You win!")
    
    elif(computer_choice == -1 and user == 0):
        print("You lose!")

    elif(computer_choice == 1 and user == 0):
        print("You win!")

    elif(computer_choice == 1 and user == -1):
        print("You lose!")

    elif(computer_choice == 0 and user == 1):
        print("You lose!")

    elif(computer_choice == 0 and user == -1):
        print("You win!")

    else:
        print("Something went wrong!")

 