answer=6
print("Welcome to the guessing game!!")

print("Please guess a number between 1 to 10: ")
guess=int(input())

if guess<answer:
    print("please guess higher!")
    guess = int(input())
    if guess == answer:
        print("You've guessed it right!")
    else:
        print("Better luck next time :(")
elif guess>answer:
    print("please guess lower!")
    guess = int(input())
    if guess == answer:
        print("You've guessed it right!")
    else:
        print("Better luck next time :(")
else:
    print("Yayy!! You've guessed the right answer in first attempt:)")