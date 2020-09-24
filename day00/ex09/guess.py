import random

secret_num = 2#random.randint(0, 99)


print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")
count = 1
while True:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess == "exit":
        print("Goodbye!")
        exit()
    if guess.isnumeric() == False:
        print("That's not a number.")
    elif int(guess) == secret_num:
        if secret_num == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if count == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print("Congratulations, you've got it!")
            print("You won in %d attemps" % (count))
        exit()
    elif int(guess) > secret_num:
        print("Too high!")
    elif int(guess) < secret_num:
        print("Too low!")
    count += 1
