name = input("What is your name? ")

print(f"Welcome {name} to this Adventure!")

answer = input("You are on a dirt road, it has come to a end and you can either go left or right. Which way do you wanna go? ").lower()


if answer == "right":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around or swim to swim accross: ").lower()
    if answer == "swim":
        print("You swam accross and got eaten by an alligator.")
        quit()
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
        
    else:
        print("Not a valid option. You lose")
        
elif answer =="left":
    answer = input("You come to a bridge, it looks fragile, do you want to cross it or head back (cross/back)?").lower()
    if answer == "back":
        print("You go Back and lose the game")
    elif answer =="cross":
        answer = input("You cross the bridge and meet a stranger. do you talk to them (yes/no)?").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you THE KEY. YOU WON!")
        elif answer == "no" :
            print("You ignore the stranger which offended them which made you LOSE!")
        else:
            print("Not a valid option. You lose")
        
    
    else:
        print("Not a valid option. You lose")
else:
    print("Not a valid option. You lose")
    
print("Thank you for playing this game", name)