print("Welcome to the Quiz")

playing=input("Do you want to play")

if playing.lower() != 'yes':
    quit()

print("Okay! lets play")

score=0


# Question 1
answer=input("What does CPU stands for?")

if answer.lower() == "central processing unit":
    print('Correct')
    score+=1

else:
    print("Incoreect")

#Question 2

answer=input("What does GPU stands for?")

if answer.lower() == "graphics processing unit":
    print('Correct')
    score+=1
else:
    print("Incoreect")

#Question 3

answer=input("What does RAM stands for?")

if answer.lower() == "random access memory":
    print('Correct')
    score+=1
else:
    print("Incoreect")

print("Marks Obtained By Player =",score)    
print("The percentage obtained by the player =" ,str(score/3*100))


