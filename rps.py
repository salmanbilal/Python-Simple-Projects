
# Rock-Paper-Scissors

"""
About:
Date: 24/06/2021
Programmer: Salman Bilal
https://www.twitter.com/SalmanB34055398
"""

import random
import time

i = 0
my_score = 0
computer_score = 0

while i < 10:
    choose = input("Choose: ")
    player2 = ["Rock", "Paper", "Scissors"]
    player2_choose = random.choice(player2)

    if (choose == "r" and player2_choose == "Rock"):
        print("You choose Rock and Computer also Choose Rock")
        print("Hence, Draw")
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "p" and player2_choose == "Paper"):
        print("You choose Paper and Computer also Choose Paper")
        print("Hence, Draw")
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "s" and player2_choose == "Scissors"):
        print("You choose Scissors and Computer also Choose Scissors")
        print("Hence, Draw")
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "r" and player2_choose == "Paper"):
        print("You choose Rock and Computer Choose Paper")
        print("Hence, You Lose")
        computer_score+=1
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "r" and player2_choose == "Scissors"):
        print("You choose Rock and Computer Choose Scissors")
        print("Hence, You Won")
        my_score+=1
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "p" and player2_choose == "Scissors"):
        print("You choose Paper and Computer Choose Scissors")
        print("Hence, You Lose")
        computer_score+=1
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "p" and player2_choose == "Rock"):
        print("You choose Paper and Computer Choose Stone")
        print("Hence, You Won")
        my_score+=1
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "s" and player2_choose == "Rock"):
        print("You choose Scissors and Computer Choose Rock")
        print("Hence, You Lose")
        computer_score+=1
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    elif (choose == "s" and player2_choose == "Paper"):
        print("You choose Scissors and Computer Choose Paper")
        print("Hence, You Won")
        my_score+=1
        print(f"You: {my_score} Computer: {computer_score}")
        i+=1

    else:
        pass

print()
print("Result is printing:")
time.sleep(2.5)
print()

print("-------------------------------------------------------------------------------------------")

if (computer_score < my_score):
    print("You won the Match")
    print(f"Your Score: {my_score} Computer Score: {computer_score}")
    print("Congrats...")

elif (computer_score > my_score):
    print("You lose the Match")
    print(f"Your Score: {my_score} Computer Score: {computer_score}")
    print("Better Luck next Time...")

elif (computer_score == my_score):
    print("Draw!")
    print(f"Your Score: {my_score} Computer Score: {computer_score}")

print("-------------------------------------------------------------------------------------------")
