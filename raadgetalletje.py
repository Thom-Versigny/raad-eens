import random
loop = True
tries = 0
Played = 0
score = 0
print("welcome to the guessing game. try to guess a random number in between 0 and 1000")
while  True:
    randomnumber = random.randint(0, 1000)
    tries = 0
    while tries < 10:
        guess = int(input("try to guess: "))
        difference = randomnumber - guess
        if difference == 0:
            print("you guessed it!")
            score += 1
            Played = 19
            break
        if difference >= -20 and difference <= 20:
            print("you are very close")
        elif difference >= -50 and difference <= 50:
            print("you are close")
        else:
            print("you are not even close")
        if guess > randomnumber:
            print("you want to go lower")
        elif guess < randomnumber:
            print("you want to go higher")
        if tries == 10:
            print("you tried but it's was:",randomnumber)
            Played = 19
        tries += 1
    print("your score: "+ str(score))
    Played+=1
    if Played == 20:
        again = input("do you want to try again? Y/N").lower()
        if again == "y":
            loop = True
            Played = 0
        elif again == "n":
            loop = False
    if loop == False:
        break
print("endscore: "+ str(score))
input("press enter to exit")

