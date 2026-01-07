import random
print("Welcome to the Coin Guessing Game!")
print("Choose a method to toss the coin:")
print("1.Using random.random()")
print("2.Using random.randint()")
choice = input("Enter your choice 1 or 2: \n")
om = random.random()
int = random.randint(0, 1)
if choice == "1":
    if om >= 0.5:
        computer_choice = "heads"
    else:
        computer_choice = "tails"
elif choice == "2":
    if int == 0:
        computer_choice = "heads"
    else:
        computer_choice = "tails"
else:
    print("The number is invalid!!")
mine = input("Enter your Guess: Heads or Tails: \n").lower()
if mine.lower() == computer_choice.lower():
    print("Congratiolations!!! You Won!")
else:
    print("Sorry, you lost!")
    print(f"The computer chose {computer_choice}")

