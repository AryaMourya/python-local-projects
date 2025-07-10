import random

user_win=0
computer_win=0

options = ["Rock","Paper","Scissors"]

while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
 
    if user_input not in ["Rock","Paper","Scissors"]:
        continue
    random_number = random.randint(0,2)
    '''rock= 0
       paper=1
       sicssors=2'''   
    computer_pick = options[random_number]
    print(f"compter picked = {computer_pick} .")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You Wins!")
        user_win += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Wins!")
        user_win += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Wins!")
        user_win += 1
        continue

    else:
        print("You Lost ")
        computer_win += 1
        continue

print(f"You won {user_win},times")
print(f"You lost {computer_win}, times")

print("GoodBye!")