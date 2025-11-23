import random 

print("Hello to the Number Guessing Game ")
top_of_range =  input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger then 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0,top_of_range)

print(f"A number has been selected randomly between 0 and {top_of_range} (both included) and you'll have to guess it")
guesses = 0

while 1:
    guesses += 1
    user_guess = input("Make A Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == random_number:
        print("You Got it")
        break
    elif user_guess > random_number :
        print("You have guessed higher then the correct number")
    else:
        print("You have guessed lower then the correct number")
        
print(f"You got it in {guesses} guesses")    