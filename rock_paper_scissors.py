import random

user_wins , computer_wins = 0 , 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print("Computer picked " + computer_input + ".")
    
    if user_input == computer_input:
        print("it's a tie")
    elif user_input == "rock" and computer_input == "scissors":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_input == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "paper":
        print("You Won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1 
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
        