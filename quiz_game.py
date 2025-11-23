print("Welcome to my computer quiz!")

playing = input("Would like to play? ")

if playing.lower() != "yes":
    quit()

print("Okey! Let's play :)")

score = 0

# First question 

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score +=1 
else:
    print("Your answer is incorrect!")
    
# Second question 

answer = input("What does GPU stand for? ")

if answer.lower() == "graphical processing unit":
    print("Correct!")
    score +=1 
else:
    print("Your answer is incorrect!")
    
# Third question 

answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score +=1 
else:
    print("Your answer is incorrect!")

# Fourth question 

answer = input("What does PSU stand for? ")

if answer.lower() == "power supply unit":
    print("Correct!")
    score +=1 
else:
    print("Your answer is incorrect!")
    
print(f"You have finished the game with the following score : ",score)

print("You got " + str(score) + " questions correct!")

print("You got " + str(  (score/4)*100  ) + "%.")