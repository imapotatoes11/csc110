number = 2561
guess = -1
while guess != number:
    guess = int(input("Guess a number: "))
    if guess != number:
        print("Too high... guess again!" if guess > number else "Too low... guess again!")
print("You got the number!")

# prof solution
jackpot = 3752
print("Let's play Needy or Greedy!")

# ask the user for an amount
guess = int(input("What's your guess?"))
# is it the amount? If so, print congrats.
while guess != jackpot:
    # otherwise, tell them high or low
    if guess > jackpot:
        print("Too high")
    else:
        print("Too low")
    # ask them to guess again
    guess = int(input("What's your guess!"))

print(f"Congratulations, you sin ${jackpot}")
