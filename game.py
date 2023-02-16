
from random import randint
#get user input
username=(input("Enter name:"))
print("Hello there "+ username + "!" )
counter=0
while counter<5:
    number=eval(input("Enter number:"))
    #generate a random number
    random=randint(10,50)
    counter+=1
    if number<random:
        print("Your guess is too low")
    elif number>random:
        print("Your guess is too high")
    elif number==random:
        print("You Win!!")
    break
if number==random:
    print("You win!!!")
else:
    print("Game Over!!!")
    print("Correct answer was:",random)
