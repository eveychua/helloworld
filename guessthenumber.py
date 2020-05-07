import random

highest = 10
answer = random.randint(1, highest)
guess = ""
countguess = 0

while guess != answer and userquit != "exit":
    guess = input("Please guess a number between 1 to {}".format(highest))
    countguess += 1
    if guess.casefold() == "exit":
        print("You have exited the game")
        break
    else:
        guess = int(guess)
        if guess == answer:
            print("Congratulations! The answer is {}. You have got the answer in {} tries!".format(answer,countguess))
            break
        elif guess > answer:
            print("Please guess lower")
        elif guess < answer:
            print("Please guess higher")
        else:
            break